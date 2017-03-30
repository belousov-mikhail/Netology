# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 23:34:35 2017

@author: Mikhail Belousov
"""
import vk
import networkx as nx


def getFriendsList (vkapi, user_id):
    raw_friends = vkapi.friends.get(user_id=user_id, fields='domain')
    friends = []
    for el in raw_friends:
        if 'deactivated' not in el.keys():
            friends.append((el['user_id'], el['last_name'], el['first_name']))
    return friends


def addToGlobal(global_dict, to_add):
    for el in to_add:
        if el[0] not in global_dict.keys():
            global_dict[el[0]] = (el[1], el[2])
    return(global_dict)


def friendsToGraph(graph, start_node, friends):
    edges_to_add = [(start_node, el) for el in friends]
    graph.add_edges_from(edges_to_add)
    return graph

def mostPopular(graph, n):
    degree_dict = dict (graph.degree_iter())
    most_popular = sorted(degree_dict.items(), key=lambda x: x[1],
              reverse=True)[0:n]
    return most_popular


def printTop (global_dict, most_popular):
    print ('Список из {} человек с максимальным количеством пересечений'.format(len(most_popular)))
    for el in most_popular:
        id = el[0]
        print ("{0} {1} связан(а) с {2} человек, id={3}".format(global_dict[id][0], global_dict[id][1], el[1], id))


def main():
    session = vk.Session()
    vkapi = vk.API(session)
    HOST_ID = 4118181
    host_data = vkapi.users.get(user_id=HOST_ID, fields='domain')[0]
    host = (HOST_ID, host_data['last_name'], host_data['first_name'])
    global_dict = {}
    global_dict[host[0]] = (host[1], host[2])
    g = nx.Graph()
    host_friends = getFriendsList(vkapi, HOST_ID)
    global_dict = addToGlobal(global_dict, host_friends)
    g = friendsToGraph(g, host[0], host_friends)
    for el in host_friends:
        more_friends = getFriendsList(vkapi, el[0])
        global_dict = addToGlobal(global_dict, more_friends)
        g = friendsToGraph(g, el[0], more_friends)
    print (nx.info(g))
    limit = int (input ("Какое количество самых популярных друзей вывести?\n>>"))
    most_popular = mostPopular(g, 50)
    printTop(global_dict, most_popular)










