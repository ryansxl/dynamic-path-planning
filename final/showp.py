import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

def showpath(airports, path, pos, color ) :
	print(path)
	pathpos= {}

	for i in path :
		pathpos.update({i: pos[i]} )
	nx.draw_networkx_nodes(airports, pathpos, path, node_size=25, node_color=color,with_labels=True)

	pathedges=[]
	for index in range (len(path)-1) :
		pathedges.append([path[index] , path[index+1] ])
	nx.draw_networkx_edges(airports, pos, pathedges, width=1.0, edge_color=color) 


def showdian(airports, dian , pos, color) :
	feiji2={}
	feiji2.update({dian: pos[dian]} )
 
	fj2=[dian]
	nx.draw_networkx_nodes(airports,feiji2, fj2 ,node_size=20,node_color=color ,with_labels=True)
