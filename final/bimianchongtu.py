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


def shortest_path1(airports, start, goal, pos, tim, chongtudian, chongtuplane, chongtuplanetime, chongtuplanezhonglei, chongtuwaittime, chongtutime2, chongtudian2,jgtime) :

	open_queue = PQueue()
	open_dict = {}
	close_dict = {}
	start_h = cal_dist(start, goal, pos)
	start_node = node(start, None, tim, start_h)
	open_queue.put((start_node.g, start_node))
	open_dict[start] = start_node

	while goal not in close_dict and not open_queue.empty():
		find_path1(airports, open_queue, open_dict, close_dict, goal, pos, tim, chongtudian, chongtuplane, chongtuplanetime, chongtuplanezhonglei, chongtuwaittime, chongtudian2, chongtutime2, jgtime)


	path = []

	if goal in close_dict:
		current_node = close_dict[goal]
		while current_node.parent != None:
			path.append(current_node.index)
			current_node = current_node.parent
		path.append(start)
		path = [path[len(path) - i -1] for i in range(len(path))]
	
	chang=[]
	for index in range(len(path)):
		mmm = close_dict[path[index]].g
		chang.append (mmm)
	
	jieguo=[]
	jieguo.append(path)
	jieguo.append(chang)
	return jieguo





def find_path1(airports, open_queue, open_dict, close_dict, goal, pos, tim, chongtudian, chongtuplane, chongtuplanetime, chongtuplanezhonglei, chongtuwaittime, chongtudian2, chongtutime2, jgtime) :

	current_node = open_queue.get()[1]
	open_dict.pop(current_node.index)
	roads = list ( nx.neighbors(airports, current_node.index ) )
	update_node = False

	for i in roads :
		if i not in close_dict :
			distance1 = cal_dist(i, current_node.index, pos)
			m=current_node.g+distance1

			if ( i in chongtudian ) and ( chongtudian.count(i) == 1 ):

				index1 = chongtudian.index(i)

				if chongtuplanezhonglei[index1] == 1 :

					t1 = chongtuplanetime[index1]
					if( m - t1 > 0 ) and ( m -t1 < jgtime) :
						ooo = jgtime - abs( m-t1 )
						new_g = m + ooo

					elif(m-t1<= 0 )  and (m -t1 >-jgtime) :
						ooo = jgtime + abs(m-t1)
						new_g = m + ooo

					else:
						new_g = m

				elif chongtuplanezhonglei[index1] == 2 :

					t1 = chongtuplanetime[index1]
					t2 = chongtutime2[index1]
					dian2 = chongtudian2[index1]
					
					distance2=cal_dist(i, dian2, pos)
					n=m+distance2

					if (m >t1 )and (m < t1+jgtime):
						ooo=jgtime- abs(m-t1)
						new_g=m+ooo

					elif (m- t1<=0)and(n-t2>=0):
						ooo=jgtime +abs(m-t1)
						new_g=m+ooo

					elif (n - t2< 0) and( n- t2 > -jgtime):
						ooo=jgtime+abs(m-t1)
						new_g=m+ooo

					else:
						new_g=m

				elif chongtuplanezhonglei[index1] == 3:
					
					t1 = chongtuplanetime[index1]
					t2 = chongtutime2[index1]
					dian2 = chongtudian2[index1]
					
					distance2=cal_dist(i, dian2, pos)
					n=m+distance2

					if (m >t1 )and (m < t1+jgtime):
						ooo= 100000
						new_g= ooo

					elif (m- t1<=0)and(n-t2>=0):
						ooo= 100000
						new_g= ooo

					elif (n - t2< 0) and( n- t2 > -jgtime):
						ooo= 100000
						new_g= ooo

					else:
						new_g= 100000


				elif chongtuplanezhonglei[index1] == 4 :

					t1 = chongtuplanetime[index1]

					ooo=jgtime+ abs(m-t1)
					new_g=m+ooo


			elif ( i in chongtudian ) and ( chongtudian.count(i) >  1 ):

				shu = chongtudian.count(i)
				ctplane=[]
				cttime=[]
				ctzhonglei=[]
				cttime2=[]
				ctdian2=[]
				shunxu = PQueue()
				mm = m

				for index in range(len(chongtudian)):
					if chongtudian[index] == i:
						ctplane.append(chongtuplane[index])
						cttime.append(chongtuplanetime[index])
						ctzhonglei.append(chongtuplanezhonglei[index])
						cttime2.append(chongtutime2[index])
						ctdian2.append(chongtudian2[index])

				for index1 in range(len(cttime)):
					shunxu.put((cttime[index1],index1))

				while( not shunxu.empty() ):
					current=shunxu.get()[1]
					

					if (ctzhonglei[current] == 1):
						

						t1 = cttime[current]
						if( mm - t1 > 0 ) and ( mm -t1 < jgtime) :
							ooo = jgtime - abs( mm-t1 )
							mm += ooo

						elif(mm-t1<= 0 )  and (mm  -t1 >-jgtime) :
							ooo = jgtime + abs(mm-t1)
							mm += ooo
					
					elif(ctzhonglei[current] == 2):

						t1 = cttime[current]
						t2 = cttime2[current]
						dian2 = ctdian2[current]
					
						distance2=cal_dist(i, dian2, pos)
						nn=mm+distance2					
					
						if (mm >t1 )and (mm < t1+jgtime):
							ooo=jgtime- abs(mm-t1)
							mm += ooo

						elif (mm- t1<=0)and(nn-t2>=0):
							ooo=jgtime +abs(mm-t1)
							mm += ooo

						elif (nn - t2< 0) and( nn- t2 > -jgtime):
							ooo=jgtime+abs(mm-t1)
							mm += ooo

					
					elif(ctzhonglei[current] == 3):

						t1 = cttime[current]
						t2 = cttime2[current]
						dian2 = ctdian2[current]
					
						distance2=cal_dist(i, dian2, pos)
						nn=mm+distance2					
					
						if (mm >t1 )and (mm < t1+jgtime):
							ooo=100000
							mm += ooo

						elif (mm- t1<=0)and(nn-t2>=0):
							ooo=100000
							mm += ooo

						elif (nn - t2< 0) and( nn- t2 > -jgtime):
							ooo=100000
							mm += ooo



				new_g = mm

			else:
				
				new_g = m



			if i in open_dict :
				if new_g < open_dict[i].g :
					open_dict[i].parent = current_node
					open_dict[i].g = new_g
					update_node = True

			else :
				new_h = cal_dist(i, goal, pos)
				new_node = node(i, current_node, new_g, new_h)
				open_dict[i] = new_node
				open_queue.put((new_node.g, new_node))


	if update_node:
		open_queue = PQueue()
		for v in open_dict.values():
			open_queue.put(( v.g, v))

	close_dict[current_node.index] = current_node

