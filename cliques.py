#!/usr/bin/env python3

import sys
import basicstats as bs
import networkx as nx
from math import *
import matplotlib.pylab as plt
import itertools as it

global graph_name
graph_name = ""
global colors, hatches
colors=it.cycle('mykwbgc')
hatches=it.cycle('/\|-+*')

def cliques_graph(graph):
	print("Description of cliques in graph " + graph_name[9:-4])
	print("Number of Cliques: " + str(len(list(nx.algorithms.clique.enumerate_all_cliques(graph)))))
	print("Number of Maximals cliques: "+ str(nx.algorithms.clique.graph_number_of_cliques(graph)))

def cliques_node(graph, node):
	print("Description of cliques in graph " + graph_name[9:-4] + " node: "+ node)
	print("Number of Cliques: " + number_of_cliques_for_node(graph, node))
	print("Number of Maximals Cliques: " + str(nx.algorithms.clique.number_of_cliques(graph, node)))
	print("Size of Largest maximal clique containing node " + str(len(nx.algorithms.clique.node_clique_number(graph))))

def description_for_every_node_in_graph(graph):
	for node in graph.nodes():
		print("\n---------------- "+ node + "'s' Cliques -----------------")
		cliques_node(graph, node)


def number_of_cliques_for_node(graph, node):
	return str(len(nx.algorithms.clique.cliques_containing_node(graph, node)))

def size_maximal_clique(graph):
	return nx.algorithms.clique.make_max_clique_graph(graph)

def draw_circle_around_clique(clique,coords):
	dist=0
	temp_dist=0
	center=[0 for i in range(2)]
	for a in clique:
		for b in clique:
			temp_dist=(coords[a][0]-coords[b][0])**2+(coords[a][1]-coords[b][1])**2
			if temp_dist>dist:
				dist=temp_dist
				for i in range(2):
					center[i]=(coords[a][i]+coords[b][i])/2
	rad=dist**0.5/2
	cir = plt.Circle((center[0],center[1]),   radius=rad*1.3,fill=False,color=color,hatch=next(hatches))
	plt.gca().add_patch(cir)
	plt.axis('scaled')
	

def draw_colored_clique_with_size_N(graph, size, circle=False):
	coords=nx.spring_layout(graph)

	cliques=[clique for clique in nx.find_cliques(graph) if len(clique)>size]

	#draw the graph
	nx.draw(graph, pos=coords, with_labels=graph.nodes().values())
	for clique in cliques:
		print("Clique to appear: ",clique)
		if circle is True:
			draw_circle_around_clique(clique, coords)
		nx.draw_networkx_nodes(graph,pos=coords,nodelist=clique,node_color=next(colors))

	plt.show()



if __name__ == '__main__':
	
	if len(sys.argv) != 2:
		print('USAGE: '+sys.argv[0]+' input.gml <model')
		exit(0)

	# pick a dataset and get some basic stats
	# graph = try_to_read_gml("datasets/word_adjacencies.gml")

	graph_name = sys.argv[1]
	G = bs.try_to_read_gml(graph_name)
	# bs.get_all_info(graph)
	
	
	
	cliques_graph(G)
	
	draw_colored_clique_with_size_N(size_maximal_clique(G), 2, False)
	draw_colored_clique_with_size_N(G, 2)
	# description_for_every_node_in_graph(G)

	