import math
import networkx as nx
from queue import PriorityQueue as PQueue

class node(object) :
	def __init__(self, index, parent, g, h):
		self.index = index
		self.parent = parent
		self.g = g
		self.h = h

	def setParent(self, parent):
		self.parent = parent
    
	def setG(self, g):
		self.g = g
    
	def setH(self, h):
		self.h = h

def cal_dist(p1, p2, pos):
	return math.sqrt((pos[p1][0] - pos[p2][0])**2 + (pos[p1][1]-pos[p2][1])**2)


def shortest_path(airports, start, goal, pos) :
	open_queue = PQueue()
	open_dict = {}
	close_dict = {}
	start_h = cal_dist(start, goal, pos)
	start_node = node(start, None, 0, start_h)
	open_queue.put((start_node.h + start_node.g, start_node))
	open_dict[start] = start_node

	while goal not in close_dict and not open_queue.empty():
		find_path(airports, open_queue, open_dict, close_dict, goal, pos)

	path = []

	if goal in close_dict:
		current_node = close_dict[goal]
		while current_node.parent != None:
			path.append(current_node.index)
			current_node = current_node.parent
		path.append(start)
		path = [path[len(path) - i -1] for i in range(len(path))]
	return path



def find_path(airports, open_queue, open_dict, close_dict, goal, pos) :
	current_node = open_queue.get()[1]
	open_dict.pop(current_node.index)
	roads = list ( nx.neighbors(airports, current_node.index ) )
	update_node = False
	for i in roads :
		if i not in close_dict :
			distance = cal_dist(i, current_node.index, pos)
			new_g = current_node.g + distance
			if i in open_dict :
				if new_g < open_dict[i].g :
					open_dict[i].parent = current_node
					open_dict[i].g = new_g
					update_node = True

			else :
				new_h = cal_dist(i, goal, pos)
				new_node = node(i, current_node, new_g, new_h)
				open_dict[i] = new_node
				open_queue.put((new_node.h + new_node.g, new_node))

	if update_node:
		open_queue = PQueue()
		for v in open_dict.values():
			open_queue.put((v.h + v.g, v))

	close_dict[current_node.index] = current_node

