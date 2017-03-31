# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 23:34:35 2017

@author: Mikhail Belousov
"""
import vk
import networkx as nx
import os
import numpy
import matplotlib.pyplot as plt

#used for authorised session
#from my_vk import MyVkData as my
#
#session = vk.AuthSession(app_id=my.APP_ID, user_login=my.HOST_LOGIN, user_password=my.getPass())
#vkapi = vk.API(session)

#used for unautorised session
session = vk.Session()
vkapi = vk.API(session)

def getVKFriends(id):
    """ input: int id
        output: dict friends of sprecified id"""
    raw_friends = vkapi.friends.get(user_id=id, fields='domain')
    friends_dict, friends_list = {}, []
    for el in raw_friends:
        if 'deactivated' not in el.keys():
            friends_dict[el['user_id']]= {'last_name': el['last_name'],'first_name': el['first_name']}
            friends_list.append(el['user_id'])
    return friends_dict, friends_list


def getAllFriends (host_id):
    """input: int host_id
        output: dict all_friends of friends and friends of friends of a host_id
                list friends_list of each friend's friends"""
    host_data = vkapi.users.get(user_id=host_id, fields='domain')[0]
    all_friends = {host_id: {'last_name': host_data['last_name'], 'first_name': host_data['first_name']}}
    host_friends_dict, host_friends_list = getVKFriends(host_id)
    all_friends.update(host_friends_dict)
    friends_lists = [(host_id, host_friends_list)]
    for el in host_friends_list:
        el_friends_dict, el_friends_list = getVKFriends(el)
        friends_lists.append((el, el_friends_list))
        all_friends.update(el_friends_dict)
    return all_friends, friends_lists


def getIntersections(friends_lists):
    """input - list friends_list of each friend's friends
       output - list inters of intersections between all friends' lists"""
    inters = []
    for i, first in enumerate (friends_lists):
        if i == (len(friends_lists)-1): break
        for second in friends_lists[i+1:]:
            inter = set(first[1]).intersection(set(second[1]))
            if inter:
                entry = (first[0], second[0], len(inter))
                inters.append(entry)
    return (inters)


def makeFListsGraph(friends_lists):
    """input - list friends_list of each friend's friends
        output - graph g of each friend's friends  where
        node atribute 'size' - is a number of friend's friedns
        egde attribute 'weight' - is a number of intersections"""
    g = nx.Graph()
    inters = getIntersections(friends_lists)
    for link in inters:
        g.add_edge (link[0], link[1], weight = link[2])
    for el in friends_lists:
        g.node[el[0]]['size']=len(el[1])
    return g


def plotGraph(g):
    """input - graph g of each friend's friends
    plots and saves the graph"""
    pos = nx.spring_layout(g, k=1)
    nodesize = [g.node[i]['size'] for i in g.nodes()]
    edge_mean = numpy.mean([g.edge[i[0]][i[1]]['weight'] for i in g.edges()])
    edge_std_dev = numpy.std([g.edge[i[0]][i[1]]['weight'] for i in g.edges()])
    edgewidth = [((g.edge[i[0]][i[1]]['weight'] - edge_mean)/edge_std_dev) for i in g.edges()]
    nx.draw_networkx_nodes(g, pos, node_size=nodesize, node_color='brown', alpha=0.6, with_labels=False)
    nx.draw_networkx_edges(g, pos, width=edgewidth, edge_color='red')
    whole_file_name = os.path.join (os.getcwd(), 'social_graph')
    plt.savefig(whole_file_name)
    plt.show()


def main(host_id=4118181):
    all_friends_dict, friends_lists = getAllFriends (host_id)
    g = makeFListsGraph (friends_lists)
    plotGraph (g)









