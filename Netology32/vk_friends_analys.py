# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 23:34:35 2017

@author: Mikhail Belousov
"""
import vk
import networkx as nx
import os


def getFriendsList (vkapi, user_id):
    raw_friends = vkapi.friends.get(user_id=user_id, fields='domain')
    friends = []
    for el in raw_friends:
        if 'deactivated' not in el.keys():
            friends.append((el['user_id'], el['last_name'], el['first_name']))
    return friends


def friendsToGraph(graph, start_node, friends):
    edges_to_add = [(start_node, el) for el in friends]
    graph.add_edges_from(edges_to_add)
    return graph


def mostPopular(graph, n):
    degree_dict = dict (graph.degree_iter())
    most_popular = sorted(degree_dict.items(), key=lambda x: x[1],
              reverse=True)[0:n]
    return most_popular


def printTop (most_popular):
    print ('Список из {} человек с максимальным количеством пересечений'.format(len(most_popular)))
    for el in most_popular:
        print ("{0} {1} связан(а) с {2} человек, id={3}".format(el[0][1], el[0][2], el[1], el[0][0]))


def saveGraph(graph):
    export_to = 'vk_graph.gexf'
    whole_file_name = os.path.join (os.getcwd(), export_to)
    nx.write_gexf(graph, whole_file_name)


def main():
    session = vk.Session()
    vkapi = vk.API(session)
    HOST_ID = 4118181
    host_data = vkapi.users.get(user_id=HOST_ID, fields='domain')[0]
    host = (HOST_ID, host_data['last_name'], host_data['first_name'])
    g = nx.Graph()
    host_friends = getFriendsList(vkapi, HOST_ID)
    g = friendsToGraph(g, host, host_friends)
    for el in host_friends:
        more_friends = getFriendsList(vkapi, el[0])
        g = friendsToGraph(g, el, more_friends)
    saveGraph(g)
    limit = int(input("Какое количество самых популярных друзей вывести?\n>>"))
    most_popular = mostPopular(g, limit)
    printTop(most_popular)


if __name__ == '__main__':
    main()









