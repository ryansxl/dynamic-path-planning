import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import pickle
from queue import PriorityQueue as PQueue

from jingtai1 import node, cal_dist, shortest_path, find_path


class airplane (object) :
	def __init__(self, index, zhong, qd, zd, time, pri, path, chang):
		self.index = index
		self.zhong=zhong
		self.qd = qd
		self.zd = zd
		self.time = time
		self.pri=pri
		self.path=path
		self.chang=chang


def airplanetxt (airports, pos, dian, zhongdian, zhong, tim, pri, planeindex, jinjiqingkuang):
	
	lenths=[]
	paths=[]

	for index in range (len(planeindex)):
		
		chang=[]
		path= shortest_path(airports, dian[index], zhongdian[index],pos)
		lenth=tim[index]
		chang.append(lenth)
		
		for index1 in range (len(path)-1) : 
			mmm = cal_dist(path[index1] , path[index1 + 1] , pos)
			lenth = lenth + mmm
			chang.append(lenth)

		paths.append(path)
		lenths.append(chang)
		print(planeindex[index])
		print(path)
		print(chang)
	

	plane_dic={}
	plane_queue = PQueue()	
	
	for index in range(len(pri))  :
		plane =  airplane  (planeindex[index],zhong[index],dian[index],zhongdian[index],tim[index],pri[index],paths[index],lenths[index])
		plane_dic[ planeindex[index] ] = plane
	
		plane_queue.put((pri[index], plane))

	with open('airplane.pickle', 'wb') as k:
		pickle.dump(plane_dic, k, pickle.HIGHEST_PROTOCOL)
		#pickle.dump(plane_queue, k, pickle.HIGHEST_PROTOCOL)
		pickle.dump(jinjiqingkuang, k, pickle.HIGHEST_PROTOCOL)
		pickle.dump(planeindex, k, pickle.HIGHEST_PROTOCOL)
		pickle.dump(pri, k, pickle.HIGHEST_PROTOCOL)
		pickle.dump(dian, k, pickle.HIGHEST_PROTOCOL)
		pickle.dump(zhongdian, k, pickle.HIGHEST_PROTOCOL)
		pickle.dump(zhong, k, pickle.HIGHEST_PROTOCOL)
		pickle.dump(tim, k, pickle.HIGHEST_PROTOCOL)
		pickle.dump(paths, k, pickle.HIGHEST_PROTOCOL)
		pickle.dump(lenths, k, pickle.HIGHEST_PROTOCOL)



with open('airport.pickle', 'rb') as f:
	airports = pickle.load(f)
	pos = pickle.load(f)

dian=['w1',202,901,'w1',504,'w1',501,502,'w1','w1']
zhongdian=[601,'r1','r1',702,'r1',703,'r1','r1',602,401]
zhong=[1,0,0,1,0,1,0,0,1,1]
tim=[0,300,105,200,0,400,300,250,25,500]
pri=[1,7,4,5,2,9,8,6,3,10]
planeindex=['CA405','3U8849','CZ3183','CA1419','PN6237','3U8935','3U8741','CA2158','3U8633','CA4123']

airplanetxt (airports, pos, dian, zhongdian, zhong, tim, pri, planeindex,0)





