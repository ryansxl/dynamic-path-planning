import pickle
import networkx as nx
from queue import PriorityQueue as PQueue
import math
import numpy as np
import matplotlib.pyplot as plt

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

def cal_dist(p1, p2, pos):
	return math.sqrt((pos[p1][0] - pos[p2][0])**2 + (pos[p1][1]-pos[p2][1])**2)

def greedy(airports,goal,now,pos):
    roads = list ( nx.neighbors(airports, now) )
    mins = 1000000
    minpoint = []
    for point in roads:
        mm = cal_dist(point,goal,pos)
        if mm < mins:
            mins = mm
            minpoint.clear()
            minpoint.append(point)
        elif mm == mins:
            minpoint.append(point)
    result=[]
    result.append(mins)
    result.append(minpoint)
    return(result)

def episode(airports,start,goal,pos,epi,q):
    alpha = 0.5
    gama = 1
    state = start
    time0 = 0
    #result = greedy(airports,goal,now,pos)
    re1 = q[state]
    vals = re1.values()
    keys = re1.keys()
    val0 = max(vals)
    roads = list ( nx.neighbors(airports, state))
    for index in jinzhi:
        if index in roads:
            roads.remove(index)
    #minpoints = result[1]
    #num1 = len(roads)
    #num2 = len(minpoints)
    if np.random.binomial(1,epi) == 1:
        action = np.random.choice(roads)
    else:
        action = np.random.choice([key for key,value in re1.items() if value == val0])
    
    while(state!=goal):
        nextstate = action
        re2 = q[nextstate]
        vals2 = re2.values()
        roads2 = list ( nx.neighbors(airports, nextstate))
        #print('aaaa')
        for index in jinzhi:
            if index in roads2:
                roads2.remove(index)
        #print(roads2)
        val2 = max(vals2)
        if np.random.binomial(1,epi) == 1:
            nextaction= np.random.choice(roads2)
        else :
            nextaction = np.random.choice([key for key,value in re2.items() if value == val2])
        reward = cal_dist(state,nextstate,pos)
        time0 += reward
        #print(state,action,nextstate,nextaction)
        q[state][action]=q[state][action]+alpha*(-reward+q[nextstate][nextaction]-q[state][action])
        state = nextstate
        action = nextaction
    return time0
        

        
with open('airport.pickle', 'rb') as f:
	airports = pickle.load(f)
	pos = pickle.load(f)


'''
q={}
for point0 in list1:
    roads = list ( nx.neighbors(airports, point0) )
    q[point0]={}
    for point1 in roads:
        if point1 not in jinzhi:
            q[point0][point1]=0
#print(q['a'])

for i in range(episodes):
    episode(airports,'w1','h',pos,0.1,q)

newstate = 'w1'
newgoal = 'h'
path=[newstate]
print(q)

while newstate!= newgoal:
    re9 = q[newstate]
    vals9 = re9.values()
    val9 = max(vals9)
    nextaction = np.random.choice([key for key,value in re9.items() if value == val9])
    path.append(nextaction)
    newstate = nextaction
print(path)
'''
    

episodes=1000
dian=['w1','b','k','w1','g','w1','g','g','w1','w1']
zhongdian=['h','r1','r1','i','r1','i','r1','r1','h','f']
times=[194.72135955,80,250,213.595559989,150,213.595559989,150,150,194.72135955,139.72135955]
results=[]
time=[[0 for i in range(episodes)] for j in range(len(dian))]
runs=50
x=list(range(1,episodes+1))

for index in range (len(dian)):
        iii=0
        for run in range(runs):
                q={}
                for point0 in list1:
                    roads = list ( nx.neighbors(airports, point0) )
                    q[point0]={}
                    for point1 in roads:
                        if point1 not in jinzhi:
                            q[point0][point1]=0
                newstate = dian[index]
                newgoal = zhongdian[index]
                path=[newstate]
                for i in range(episodes): 
                        time0 = episode(airports,newstate,newgoal,pos,0.1,q)
                        time[index][i] += time0/runs
                        iii+=1
                        #print(iii)
        newstate = dian[index]
        newgoal = zhongdian[index]
        path=[newstate]
        while newstate!= newgoal:
            re9 = q[newstate]
            vals9 = re9.values()
            val9 = max(vals9)
            nextaction = np.random.choice([key for key,value in re9.items() if value == val9])
            path.append(nextaction)
            newstate = nextaction
        print("start ",dian[index],'end ',zhongdian[index])
        print(path)
        results.append(path)

print('jieshule')
for index in range(len(dian)):
        plt.plot(x,time[index])

plt.ylabel('Length of the path')
plt.xlabel('Episodes')
plt.show()
        
    
