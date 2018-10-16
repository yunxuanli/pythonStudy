# coding = utf-8
import networkx as nx 
import matplotlib.pyplot as plt
import csv


edge = []

import pandas as pd 
edgeDataframe = pd.read_csv("edge.csv",encoding="utf-8")
print(edgeDataframe)
for i in range(1,len(edgeDataframe)):
	line = tuple([edgeDataframe['Source'][i],edgeDataframe['Target'][i]])
	#print(f"line:{line}")
	edge.append(line)
print(edge)

G = nx.Graph()
#G.add_nodes_from(id_tag)
G.add_edges_from(edge)
#print(f"edge:{edge}")

colors = ["red","green","blue","yellow"]


#nx.draw(G,with_labels=True,pos=nx.random_layout(G),font_size=12,node_size=2000,node_color=colors) #alpha=0.3
#pos=nx.spring_layout(G,iterations=50)
pos=nx.random_layout(G)
nx.draw_networkx_nodes(G, pos, alpha=0.2,node_size=1200,node_color=colors)
nx.draw_networkx_edges(G, pos, node_color='r', alpha=0.3) #style='dashed'
nx.draw_networkx_labels(G, pos, font_family='sans-serif', alpha=0.5) #font_size=5
plt.show()