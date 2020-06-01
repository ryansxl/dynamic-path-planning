import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import pickle
from queue import PriorityQueue as PQueue
import math


wnlist=['w1','w2','w3','w4','w5','w6','w7','w8','w9','w10','w11']
rnlist=['r1','r2','r3','r4','r5','r6','r7','r8','r9','r10','r11','r12','r13']
qnlist=['q1','q2','q3','q4','q5','q6','q7','q8','q9','q10','q11','q12']
aanlist=['m','n','r','s','t','u','v','w','x','y','z','z1','z2','z3','z4','z5']
bbnlist=['l','k','j','i','h','g','f','e','c','b','a']
anlist=['a0','a1','a2','a3','a4','a5','a6','a7','a8','a9','a10']
bnlist=['b0','b1','b2','b3','b4','b5','b6']
cnlist=['c0','c1','c2','c3','c4','c5']
fnlist=['f0','f1','f2','f3']
gnlist=['g0','g1','g2','g3','g4','g5','g6','g7']
hnlist=['h0','h1','h2','h3','h4','h5','h6','h7']
inlist=['i0','i1','i2','i3','i4','i5','i6','i7','i8']
jnlist=['j0','j1','j2','j3','j4']
knlist=['k0','k1','k2','k3','k4','k5','k6']

jinzhi = ['a0','b0','c0','f0','g0','h0','i0','j0','k0']

list1 = wnlist+rnlist+qnlist+aanlist+bbnlist
list2 = anlist+bnlist+cnlist+fnlist+gnlist+hnlist+inlist+jnlist+knlist


from bimianchongtu import node, cal_dist, shortest_path1, find_path1

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
	

class waitinfo (object) :
    def __init__(self, index, waitplace, timeofwait, zhonglei, waittime):
	self.index=index
        self.waitplace=waitplace
        self.timeofwait=timeofwait
	self.zhonglei=zhonglei
	self.waittime=waittime


def cal_dist(p1, p2, pos):
	return math.sqrt((pos[p1][0] - pos[p2][0])**2 + (pos[p1][1]-pos[p2][1])**2)


with open('airport.pickle', 'rb') as f:
	airports = pickle.load(f)
	pos = pickle.load(f)
	pdpos = pickle.load(f)
	hxpos = pickle.load(f)
	tjpos = pickle.load(f)
	pdlist = pickle.load(f)
	hxlist = pickle.load(f)
	tjlist = pickle.load(f)
	pedges = pickle.load(f)
	hedges = pickle.load(f)
	ledges = pickle.load(f)

with open('airplane2.pickle', 'rb') as k:
	
	plane_dic=pickle.load(k)
	#print(plane_dic)
	jinjiqingkuang=pickle.load(k)
	#print('aaaaa')
	#print(jinjiqingkuang)
	planeindex=pickle.load(k)
	#print('bbbbb')
	#print(planeindex)
	pri=pickle.load(k)
	#print('ccccc')
	#print(pri)
	dian=pickle.load(k)
	#print('ddddd')
	#print(dian)
	zhongdian=pickle.load(k)
	#print(zhongdian)
	zhong=pickle.load(k)
	#print(zhong)
	tim=pickle.load(k)
	#print(tim)
	paths=pickle.load(k)
	#print('eeeee')
	#print(paths)
	lenths=pickle.load(k)
	#print('fffff')
	#print(lenths)
	#print('iuahdfsiu')
	#print(plane_dic['3U8741'])



def finds(airports,pos,finishplanes,currentplane,finishplanedic,currentnode,nextnode,currenttime,jgtime):
    chongtu = False
    ppp = []
    len1 = cal_dist(currentnode,nextnode,pos)
    for index in range(len(finishplanes)):
        plane0 = finishplanes[index]
        #print(finishplanedic[plane0])
        path0 = finishplanedic[plane0].path
        time0 = finishplanedic[plane0].chang
        for index2 in range(len(path0)):
            if currentnode not in tjlist and currentnode !='w1' and currentnode != 'r1':
                if currentnode == path0[index2] and nextnode != path0[index2-1]:
                    if (currenttime - time0[index2])>=0 and (currenttime - time0[index2])<jgtime:

                        jcdian = currentnode
                        ooo = jgtime - abs(currenttime-time0[index2])
                        ppp.append(ooo)
                        chongtu =True
                        #print('jiaocha1')

                    elif (currenttime - time0[index2])>-jgtime and (currenttime - time0[index2])<0:

                        jcdian = currentnode
                        ooo = jgtime+abs(currenttime-time0[index2])
                        ppp.append(ooo)
                        #print('jiaocha2')
                        chongtu =True

                elif currentnode == path0[index2] and nextnode == path0[index2-1]:
                    if (currenttime - time0[index2])>=0 and (currenttime - time0[index2])<jgtime:
                        jcdian = currentnode
                        ooo =  jgtime - abs(currenttime-time0[index2])
                        ppp.append(ooo)
                        #print('duitou1')
                        chongtu =True
                    elif (currenttime - time0[index2])<0 and ((currenttime + len1) - time0[index2 - 1])>0:
                        jcdian = currentnode
                        ooo = jgtime+abs(currenttime-time0[index2])
                        ppp.append(ooo)
                        #print('duitou2')
                        chongtu =True

                    elif ((currenttime+len1) - time0[index2-1])<=0 and ((currenttime+len1) - time0[index2-1]) >-jgtime:
                        jcdian = currentnode
                        ooo=jgtime+abs(currenttime-time0[index2])
                        ppp.append(ooo)
                        #print('duitou3')
                        chongtu =True
    #print('bbbbbbbb',finishplanes)
    #print(currentplane)
    result=[]
    result.append(chongtu)
    result.append(ppp)
    #print(result)
    return result


def episode(airports,start,goal,pos,epi,q,finishplanedic,finishplanes,jgtime,currentplane,starttime):
    #print(currentplane)
    #print(finishplanes)
    alpha = 0.5
    gama = 1
    state = start
    time0 = starttime

    re1 = q[state]
    vals = re1.values()
    keys = re1.keys()
    val0 = max(vals)
    roads = list(nx.neighbors(airports,state))
    for index in jinzhi:
        if index in roads:
            roads.remove(index)

    if np.random.binomial(1,epi) == 1:
        action = np.random.choice(roads)
    else:
        action = np.random.choice([key for key,value in re1.items() if value == val0])

    while (state != goal):
        nextstate = action
        re2 = q[nextstate]
        vals2 = re2.values()
        roads2 = list ( nx.neighbors(airports, nextstate))
        for index in jinzhi:
            if index in roads2:
                roads2.remove(index)
        val2 = max(vals2)
        if np.random.binomial(1,epi) == 1:
            nextaction= np.random.choice(roads2)
        else :
            nextaction = np.random.choice([key for key,value in re2.items() if value == val2])
        len0 = cal_dist(state,nextstate,pos)
        #print(currentplane,state,nextstate)
        result = finds(airports,pos,finishplanes,currentplane,finishplanedic,state,nextstate,time0,jgtime)
        #print(result)
        #print('oooooooo')
        ppp = result[1]
        if not ppp:
            ooo = 0
        else:
            ooo = ppp[0]
        reward = len0 + ooo
        time0 += reward
        q[state][action]=q[state][action]+alpha*(-reward+q[nextstate][nextaction]-q[state][action])
        state = nextstate
        action = nextaction
    return
                
        
episodes=1000
dian=['w1','g','w1','k','w1','g','b','g','w1','w1']
zhongdian=['h','r1','h','r1','i','r1','r1','r1','i','f']
tim=[0,30,25,120,200,270,320,315,400,500]
zhong=[1,0,1,0,1,0,0,0,1,1]
pri=[1,2,3,4,5,6,7,8,9,10]
planeindex=['CA405','PN6237','3U8633','CZ3183','CA1419','CA2158','3U8849','3U8741','3U8935','CA4123']
runs=1


finishplanedic={}
finishplanes=[]


for index in range(len(pri)):
    for run in range(runs):
        q={}
        for point0 in list1:
            roads = list( nx.neighbors(airports, point0) )
            q[point0]={}
            for point1 in roads:
                if point1 not in jinzhi:
                    q[point0][point1]=0
        newstate = dian[index]
        newgoal = zhongdian[index]
        path=[newstate]
        currentplane = planeindex[index]
        starttime=tim[index]
        jgtime =10
        for i in range(episodes):
            episode(airports,newstate,newgoal,pos,0.1,q,finishplanedic,finishplanes,jgtime,currentplane,starttime)

    newstate = dian[index]
    newgoal = zhongdian[index]
    path=[newstate]
    chang=[tim[index]]
    while newstate!=newgoal:
        re9 = q[newstate]
        vals9 = re9.values()
        val9 = max(vals9)
        nextaction = np.random.choice([key for key,value in re9.items() if value == val9])
        len9 = cal_dist(newstate,nextaction,pos)
        time9 = chang[-1]
        result0 = finds(airports,pos,finishplanes,planeindex[index],finishplanedic,newstate,nextaction,time9,jgtime)
        ppp = result0[1]
        if not ppp:
            ooo = 0
        else:
            ooo = ppp[0]
        time9 = time9+ooo+len9
        chang.append(time9)
        path.append(nextaction)
        newstate = nextaction
    print("start ",dian[index],'end ',zhongdian[index])
    print(planeindex[index])
    print(path)
    print(chang)
    finishplanes.append(planeindex[index])
    plane = airplane(planeindex[index],zhong[index],dian[index],zhongdian[index],tim[index],pri[index],path,chang)
    finishplanedic[planeindex[index]]=plane
    

    
    
            
                
                
                       
                       
                       
                       




        
                       


    
	
