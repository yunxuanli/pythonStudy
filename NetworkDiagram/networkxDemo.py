# coding = utf-8
'''
    参考网址：https://github.com/maoqyhz/TextCharactervVisualization
'''
from __future__ import print_function

"""
Created on 2018/10/15 12:24

@file: relationship_view.py
@author: Kaimo Yang
"""
import networkx as nx 
import matplotlib.pyplot as plt
import csv


edge = []

inputdir = "output/"

import pandas as pd 
edgeDataframe = pd.read_csv(inputdir + "edge.csv",encoding="utf-8")
print(edgeDataframe)
for i in range(0,len(edgeDataframe)):
	line = tuple([edgeDataframe['Source'][i],edgeDataframe['Target'][i]])
	#print(f"line:{line}")
	edge.append(line)
print(edge)

G = nx.Graph()
#G.add_nodes_from(id_tag)
G.add_edges_from(edge)
#print(f"edge:{edge}")

colors = ["red","green","blue","yellow"]

pos=nx.random_layout(G)
nx.draw_networkx_nodes(G, pos, alpha=0.2,node_size=1200,node_color=colors)
nx.draw_networkx_edges(G, pos, node_color='r', alpha=0.3) #style='dashed'
nx.draw_networkx_labels(G, pos, font_family='sans-serif', alpha=0.5) #font_size=5
plt.show()