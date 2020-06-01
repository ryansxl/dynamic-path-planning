import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import pickle
from queue import PriorityQueue as PQueue



from bimianchongtu import node, cal_dist, shortest_path1, find_path1

class airplane (object) :
	def __init__(self, index, zhong, qd, zd, time, pri, path, chang, chongtudian, chongtuplane, chongtuplanetime, chongtuplanezhonglei, chongtuwaittime, chongtudian2, chongtutime2):
		self.index = index
		self.zhong=zhong
		self.qd = qd
		self.zd = zd
		self.time = time
		self.pri=pri
		self.path=path
		self.chang=chang
		self.chongtudian=chongtudian
		self.chongtuplane=chongtuplane
		self.chongtuplanetime=chongtuplanetime
		self.chongtuplanezhonglei=chongtuplanezhonglei
		self.chongtuwaittime=chongtuwaittime
		self.chongtudian2=chongtudian2
		self.chongtutime2=chongtutime2


class waitinfo (object) :
	def __init__(self, index, waitplace, timeofwait, zhonglei, waittime):
		self.index=index
		self.waitplace=waitplace
		self.timeofwait=timeofwait
		self.zhonglei=zhonglei
		self.waittime=waittime

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



def bimianchongtu2 (airports, pos, dian, zhongdian, zhong, tim, pri, planeindex, paths, lenths, jgtime)  :
 	
	plane_queue = PQueue()
	newplane_dic={}

	open_airplane = []
	close_airplane =[]

	waitplane={}
	waitplaneindex=[]
	alltime=0

	tinglist=['w1','w2','w3','w4','w5','w6','w7','w8','w9','w10','w11','r1','r2','r3','r4','r5','r6','r7','r8','r9','r10','r11','r12','r13','a0','a1','a2','a3','a4','a5','a6','a7','a8','a9','a10','b0','b1','b2','b3','b4','b5','b6','c0','c1','c2','c3','c4','c5','f0','f1','f2','f3','g0','g1','g2','g3','g4','g5','g6','g7','h0','h1','h2','h3','h4','h5','h6','h7','i0','i1','i2','i3','i4','i5','i6','i7','i8','j0','j1','j2','j3','j4','k0','k1','k2','k3','k4','k5','k6']


	for index in range(len(pri))  :
		
		chongtudian=[]
		chongtuplane=[]
		chongtuplanetime=[]
		chongtuzhonglei=[]
		chongtuwaittime=[]
		chongtudian2=[]
		chongtutime2=[]

		print(planeindex[index])
		print(zhong[index])
		print(dian[index])
		print(zhongdian[index])
		print(tim[index])
		print(pri[index])
		print(paths[index])
		print(lenths[index])


		plane =  airplane  (planeindex[index],zhong[index],dian[index],zhongdian[index],tim[index],pri[index],paths[index],lenths[index],chongtudian,chongtuplane,chongtuplanetime,chongtuzhonglei,chongtuwaittime,chongtudian2,chongtutime2)
		newplane_dic[ planeindex[index] ] = plane	
		plane_queue.put((pri[index], plane))

	
	while ( not plane_queue.empty() ):
	
		current_plane1 = plane_queue.get()[1]
		current_plane1index=current_plane1.index

		current_plane = newplane_dic[current_plane1index]
		print(current_plane.index)
		print(current_plane.path)
		print(current_plane.chang)
		o0o = 0

				
		if  len(close_airplane) :

			for index1 in range(len(close_airplane)) :
				zzzzzz=0

				if o0o >0:
					break
				elif close_airplane[index1].index != current_plane.index:

					for index2 in range(len(current_plane.path)) :

						if o0o >0:
							break

						elif (current_plane.path[index2] not in tjlist and current_plane.path[index2] !='w1' and current_plane.path[index2] != 'r1') :

							for index3 in range(len(close_airplane[index1].path)):


								if (close_airplane[index1].path[index3] not in tjlist and close_airplane[index1].path[index3] !='w1' and close_airplane[index1].path[index3] !='r1'):


									if current_plane.path[index2]==close_airplane[index1].path[index3]  and current_plane.path[index2 +1] != close_airplane[index1].path[index3 - 1] :

										if current_plane.chang[index2]-close_airplane[index1].chang[index3] >=0 and current_plane.chang[index2]-close_airplane[index1].chang[index3] < jgtime :

											print('aaaaaaaaa')
											print(current_plane.index)
											print(close_airplane[index1].index)
											print(o0o)
											o0o += 1

											print(newplane_dic[current_plane.index].path)
											print(newplane_dic[current_plane.index].chang)
											print(close_airplane[index1].path)
											print(close_airplane[index1].chang)


											jcdian=current_plane.path[index2]
											ooo=jgtime-abs(current_plane.chang[index2]-close_airplane[index1].chang[index3])
											www1=close_airplane[index1].index
											www2=close_airplane[index1].chang[index3]
											www3=1
											www4=ooo
											www5=0
											www6=0
											
											newplane_dic[current_plane.index].chongtudian.append(jcdian)
											newplane_dic[current_plane.index].chongtuplane.append(www1)
											newplane_dic[current_plane.index].chongtuplanetime.append(www2)
											newplane_dic[current_plane.index].chongtuplanezhonglei.append(www3)
											newplane_dic[current_plane.index].chongtuwaittime.append(www4)
											newplane_dic[current_plane.index].chongtutime2.append(www5)
											newplane_dic[current_plane.index].chongtudian2.append(www6)


											vvv1=newplane_dic[current_plane.index].chongtudian
											vvv2=newplane_dic[current_plane.index].chongtuplane
											vvv3=newplane_dic[current_plane.index].chongtuplanetime
											vvv4=newplane_dic[current_plane.index].chongtuplanezhonglei
											vvv5=newplane_dic[current_plane.index].chongtuwaittime
											vvv6=newplane_dic[current_plane.index].chongtutime2
											vvv7=newplane_dic[current_plane.index].chongtudian2


											newjg=shortest_path1(airports, current_plane.qd, current_plane.zd, pos, current_plane.time, vvv1, vvv2, vvv3, vvv4, vvv5, vvv6, vvv7,jgtime)
											newpath=newjg[0]
											newchang=newjg[1]
											
						
											print(jcdian)
											print(vvv1)
											print(vvv3)
											print(current_plane.chang[index2])
											print(newpath)
											print(newchang)					
		
											newplane_dic[current_plane.index].path=newpath
											newplane_dic[current_plane.index].chang=newchang
											newpri=current_plane.pri

											print(newplane_dic[current_plane.index].path)
											print(newplane_dic[current_plane.index].chang)
											
											

											zzzzzz=1
											plane_queue.put((newpri, newplane_dic[current_plane.index]))

											break



										elif current_plane.chang[index2]-close_airplane[index1].chang[index3] > -jgtime and current_plane.chang[index2]-close_airplane[index1].chang[index3] < 0 :

											print('bbbbbb')
											print(current_plane.index)
											print(close_airplane[index1].index)
											print(o0o)
											o0o += 1
											print(newplane_dic[current_plane.index].path)
											print(newplane_dic[current_plane.index].chang)
											print(close_airplane[index1].path)
											print(close_airplane[index1].chang)


											jcdian=current_plane.path[index2]
											ooo=jgtime+abs(current_plane.chang[index2]-close_airplane[index1].chang[index3])
											www1=close_airplane[index1].index
											www2=close_airplane[index1].chang[index3]
											www3=1
											www4=ooo
											www5=0
											www6=0
											
											newplane_dic[current_plane.index].chongtudian.append(jcdian)
											newplane_dic[current_plane.index].chongtuplane.append(www1)
											newplane_dic[current_plane.index].chongtuplanetime.append(www2)
											newplane_dic[current_plane.index].chongtuplanezhonglei.append(www3)
											newplane_dic[current_plane.index].chongtuwaittime.append(www4)
											newplane_dic[current_plane.index].chongtutime2.append(www5)
											newplane_dic[current_plane.index].chongtudian2.append(www6)


											vvv1=newplane_dic[current_plane.index].chongtudian
											vvv2=newplane_dic[current_plane.index].chongtuplane
											vvv3=newplane_dic[current_plane.index].chongtuplanetime
											vvv4=newplane_dic[current_plane.index].chongtuplanezhonglei
											vvv5=newplane_dic[current_plane.index].chongtuwaittime
											vvv6=newplane_dic[current_plane.index].chongtutime2
											vvv7=newplane_dic[current_plane.index].chongtudian2


											newjg=shortest_path1(airports, current_plane.qd, current_plane.zd, pos, current_plane.time, vvv1, vvv2, vvv3, vvv4, vvv5, vvv6, vvv7,jgtime)
											newpath=newjg[0]
											newchang=newjg[1]
											
						
											print(jcdian)
											print(vvv1)
											print(vvv3)
											print(current_plane.chang[index2])
									
											print(newpath)
											print(newchang)					
		
											newplane_dic[current_plane.index].path=newpath
											newplane_dic[current_plane.index].chang=newchang
											print(newplane_dic[current_plane.index].path)
											print(newplane_dic[current_plane.index].chang)
											newpri=current_plane.pri

											print('shuaixinlin')

											zzzzzz=1
											plane_queue.put((newpri, newplane_dic[current_plane.index]))

											break


									elif current_plane.path[index2]==close_airplane[index1].path[index3]  and current_plane.path[index2 +1] == close_airplane[index1].path[index3 - 1]:

										if current_plane.chang[index2]-close_airplane[index1].chang[index3] >=0 and current_plane.chang[index2]-close_airplane[index1].chang[index3] < jgtime :


											if((index2 - 1)>=0 and (index3 +1)<len(close_airplane[index1].chang)):

												if current_plane.path[index2-1]==close_airplane[index1].path[index3 +1]  and current_plane.path[index2 -1] not in tinglist:


													print('ffffff1')
													print(current_plane.index)
													print(close_airplane[index1].index)
													print(o0o)
													o0o += 1		
													print(newplane_dic[current_plane.index].path)
													print(newplane_dic[current_plane.index].chang)
													print(close_airplane[index1].path)
													print(close_airplane[index1].chang)


													jcdian=current_plane.path[index2]
													ooo=100000
													www1=close_airplane[index1].index
													www2=close_airplane[index1].chang[index3]
													www3=3
													www4=ooo
													www5=close_airplane[index1].chang[index3 -1]
													www6=close_airplane[index1].path[index3 -1]
													
													newplane_dic[current_plane.index].chongtudian.append(jcdian)
													newplane_dic[current_plane.index].chongtuplane.append(www1)
													newplane_dic[current_plane.index].chongtuplanetime.append(www2)
													newplane_dic[current_plane.index].chongtuplanezhonglei.append(www3)
													newplane_dic[current_plane.index].chongtuwaittime.append(www4)
													newplane_dic[current_plane.index].chongtutime2.append(www5)
													newplane_dic[current_plane.index].chongtudian2.append(www6)


													vvv1=newplane_dic[current_plane.index].chongtudian
													vvv2=newplane_dic[current_plane.index].chongtuplane
													vvv3=newplane_dic[current_plane.index].chongtuplanetime
													vvv4=newplane_dic[current_plane.index].chongtuplanezhonglei
													vvv5=newplane_dic[current_plane.index].chongtuwaittime
													vvv6=newplane_dic[current_plane.index].chongtutime2
													vvv7=newplane_dic[current_plane.index].chongtudian2


													newjg=shortest_path1(airports, current_plane.qd, current_plane.zd, pos, current_plane.time, vvv1, vvv2, vvv3, vvv4, vvv5, vvv6, vvv7,jgtime)
													newpath=newjg[0]
													newchang=newjg[1]
													
								
													print(jcdian)
													print(vvv1)
													print(vvv3)
													print(current_plane.chang[index2])
									
													print(newpath)
													print(newchang)					
				
													newplane_dic[current_plane.index].path=newpath
													newplane_dic[current_plane.index].chang=newchang
													print(newplane_dic[current_plane.index].path)
													print(newplane_dic[current_plane.index].chang)
													newpri=current_plane.pri


													zzzzzz=1
													plane_queue.put((newpri, newplane_dic[current_plane.index]))

													break
												

												elif current_plane.path[index2-1]==close_airplane[index1].path[index3 +1]  and current_plane.path[index2 -1]  in tinglist:


													print('gggggg1')
													print(current_plane.index)
													print(close_airplane[index1].index)
													print(o0o)
													o0o += 1		
													print(newplane_dic[current_plane.index].path)
													print(newplane_dic[current_plane.index].chang)
													print(close_airplane[index1].path)
													print(close_airplane[index1].chang)

													while ((index2-1) >=0 and (index3 +1) < len(close_airplane[index1].path)): 


														if current_plane.path[index2 -1] == close_airplane[index1].path[index3 +1]:

															index2 -=1
															index3 +=1
															
														elif(current_plane.path[index2 -1] != close_airplane[index1].path[index3 +1]):

															break



													jcdian=current_plane.path[index2]
													ooo= jgtime +abs(close_airplane[index1].chang[index3] - current_plane.chang[index2])
													www1=close_airplane[index1].index
													www2=close_airplane[index1].chang[index3]
													www3=4
													www4=ooo
													www5=0
													www6=0
													
													newplane_dic[current_plane.index].chongtudian.append(jcdian)
													newplane_dic[current_plane.index].chongtuplane.append(www1)
													newplane_dic[current_plane.index].chongtuplanetime.append(www2)
													newplane_dic[current_plane.index].chongtuplanezhonglei.append(www3)
													newplane_dic[current_plane.index].chongtuwaittime.append(www4)
													newplane_dic[current_plane.index].chongtutime2.append(www5)
													newplane_dic[current_plane.index].chongtudian2.append(www6)


													vvv1=newplane_dic[current_plane.index].chongtudian
													vvv2=newplane_dic[current_plane.index].chongtuplane
													vvv3=newplane_dic[current_plane.index].chongtuplanetime
													vvv4=newplane_dic[current_plane.index].chongtuplanezhonglei
													vvv5=newplane_dic[current_plane.index].chongtuwaittime
													vvv6=newplane_dic[current_plane.index].chongtutime2
													vvv7=newplane_dic[current_plane.index].chongtudian2


													newjg=shortest_path1(airports, current_plane.qd, current_plane.zd, pos, current_plane.time, vvv1, vvv2, vvv3, vvv4, vvv5, vvv6, vvv7,jgtime)
													newpath=newjg[0]
													newchang=newjg[1]
													
								
													print(jcdian)
													print(vvv1)
													print(vvv3)
													print(current_plane.chang[index2])
									
													print(newpath)
													print(newchang)					
				
													newplane_dic[current_plane.index].path=newpath
													newplane_dic[current_plane.index].chang=newchang
													print(newplane_dic[current_plane.index].path)
													print(newplane_dic[current_plane.index].chang)
													newpri=current_plane.pri

													zzzzzz=1
													plane_queue.put((newpri, newplane_dic[current_plane.index]))

													break
			



												elif(current_plane.path[index2-1]!=close_airplane[index1].path[index3 +1]):

													print('cccccc1')
													print(current_plane.index)
													print(close_airplane[index1].index)
													print(o0o)
													o0o += 1
													print(newplane_dic[current_plane.index].path)
													print(newplane_dic[current_plane.index].chang)
													print(close_airplane[index1].path)
													print(close_airplane[index1].chang)


													jcdian=current_plane.path[index2]
													ooo=jgtime-abs(current_plane.chang[index2]-close_airplane[index1].chang[index3])
													www1=close_airplane[index1].index
													www2=close_airplane[index1].chang[index3]
													www3=2
													www4=ooo
													www5=close_airplane[index1].chang[index3 -1]
													www6=close_airplane[index1].path[index3 -1]
													
													newplane_dic[current_plane.index].chongtudian.append(jcdian)
													newplane_dic[current_plane.index].chongtuplane.append(www1)
													newplane_dic[current_plane.index].chongtuplanetime.append(www2)
													newplane_dic[current_plane.index].chongtuplanezhonglei.append(www3)
													newplane_dic[current_plane.index].chongtuwaittime.append(www4)
													newplane_dic[current_plane.index].chongtutime2.append(www5)
													newplane_dic[current_plane.index].chongtudian2.append(www6)


													vvv1=newplane_dic[current_plane.index].chongtudian
													vvv2=newplane_dic[current_plane.index].chongtuplane
													vvv3=newplane_dic[current_plane.index].chongtuplanetime
													vvv4=newplane_dic[current_plane.index].chongtuplanezhonglei
													vvv5=newplane_dic[current_plane.index].chongtuwaittime
													vvv6=newplane_dic[current_plane.index].chongtutime2
													vvv7=newplane_dic[current_plane.index].chongtudian2


													newjg=shortest_path1(airports, current_plane.qd, current_plane.zd, pos, current_plane.time, vvv1, vvv2, vvv3, vvv4, vvv5, vvv6, vvv7,jgtime)
													newpath=newjg[0]
													newchang=newjg[1]
													
								
													print(jcdian)
													print(vvv1)
													print(vvv3)
													print(current_plane.chang[index2])
									
													print(newpath)
													print(newchang)					
				
													newplane_dic[current_plane.index].path=newpath
													newplane_dic[current_plane.index].chang=newchang
													print(newplane_dic[current_plane.index].path)
													print(newplane_dic[current_plane.index].chang)
													newpri=current_plane.pri

													zzzzzz=1
													plane_queue.put((newpri, newplane_dic[current_plane.index]))

													break




										elif current_plane.chang[index2 +1]-close_airplane[index1].chang[index3 -1 ]<=0 and  current_plane.chang[index2 +1]-close_airplane[index1].chang[index3 -1 ]> -jgtime :


											if((index2 - 1)>=0 and (index3 +1)<len(close_airplane[index1].chang)):

												if current_plane.path[index2-1]==close_airplane[index1].path[index3 +1]  and current_plane.path[index2 -1] not in tinglist:


													print('ffffff2')
													print(current_plane.index)
													print(close_airplane[index1].index)
													print(o0o)
													o0o += 1		
													print(newplane_dic[current_plane.index].path)
													print(newplane_dic[current_plane.index].chang)
													print(close_airplane[index1].path)
													print(close_airplane[index1].chang)


													jcdian=current_plane.path[index2]
													ooo=100000
													www1=close_airplane[index1].index
													www2=close_airplane[index1].chang[index3]
													www3=3
													www4=ooo
													www5=close_airplane[index1].chang[index3 -1]
													www6=close_airplane[index1].path[index3 -1]
													
													newplane_dic[current_plane.index].chongtudian.append(jcdian)
													newplane_dic[current_plane.index].chongtuplane.append(www1)
													newplane_dic[current_plane.index].chongtuplanetime.append(www2)
													newplane_dic[current_plane.index].chongtuplanezhonglei.append(www3)
													newplane_dic[current_plane.index].chongtuwaittime.append(www4)
													newplane_dic[current_plane.index].chongtutime2.append(www5)
													newplane_dic[current_plane.index].chongtudian2.append(www6)


													vvv1=newplane_dic[current_plane.index].chongtudian
													vvv2=newplane_dic[current_plane.index].chongtuplane
													vvv3=newplane_dic[current_plane.index].chongtuplanetime
													vvv4=newplane_dic[current_plane.index].chongtuplanezhonglei
													vvv5=newplane_dic[current_plane.index].chongtuwaittime
													vvv6=newplane_dic[current_plane.index].chongtutime2
													vvv7=newplane_dic[current_plane.index].chongtudian2


													newjg=shortest_path1(airports, current_plane.qd, current_plane.zd, pos, current_plane.time, vvv1, vvv2, vvv3, vvv4, vvv5, vvv6, vvv7,jgtime)
													newpath=newjg[0]
													newchang=newjg[1]
													
								
													print(jcdian)
													print(vvv1)
													print(vvv3)
													print(current_plane.chang[index2])
									
													print(newpath)
													print(newchang)					
				
													newplane_dic[current_plane.index].path=newpath
													newplane_dic[current_plane.index].chang=newchang
													print(newplane_dic[current_plane.index].path)
													print(newplane_dic[current_plane.index].chang)
													newpri=current_plane.pri



													zzzzzz=1
													plane_queue.put((newpri, newplane_dic[current_plane.index]))

													break



												elif current_plane.path[index2-1]==close_airplane[index1].path[index3 +1]  and current_plane.path[index2 -1]  in tinglist:


													print('gggggg2')
													print(current_plane.index)
													print(close_airplane[index1].index)
													print(o0o)
													o0o += 1		
													print(newplane_dic[current_plane.index].path)
													print(newplane_dic[current_plane.index].chang)
													print(close_airplane[index1].path)
													print(close_airplane[index1].chang)

													while ((index2-1) >=0 and (index3 +1) < len(close_airplane[index1].path)): 


														if current_plane.path[index2 -1] == close_airplane[index1].path[index3 +1]:

															index2 -=1
															index3 +=1
															
														elif(current_plane.path[index2-1]!=close_airplane[index1].path[index3 +1]):

															break



													jcdian=current_plane.path[index2]
													ooo= jgtime +abs(close_airplane[index1].chang[index3] - current_plane.chang[index2])
													www1=close_airplane[index1].index
													www2=close_airplane[index1].chang[index3]
													www3=4
													www4=ooo
													www5=0
													www6=0
													
													newplane_dic[current_plane.index].chongtudian.append(jcdian)
													newplane_dic[current_plane.index].chongtuplane.append(www1)
													newplane_dic[current_plane.index].chongtuplanetime.append(www2)
													newplane_dic[current_plane.index].chongtuplanezhonglei.append(www3)
													newplane_dic[current_plane.index].chongtuwaittime.append(www4)
													newplane_dic[current_plane.index].chongtutime2.append(www5)
													newplane_dic[current_plane.index].chongtudian2.append(www6)


													vvv1=newplane_dic[current_plane.index].chongtudian
													vvv2=newplane_dic[current_plane.index].chongtuplane
													vvv3=newplane_dic[current_plane.index].chongtuplanetime
													vvv4=newplane_dic[current_plane.index].chongtuplanezhonglei
													vvv5=newplane_dic[current_plane.index].chongtuwaittime
													vvv6=newplane_dic[current_plane.index].chongtutime2
													vvv7=newplane_dic[current_plane.index].chongtudian2


													newjg=shortest_path1(airports, current_plane.qd, current_plane.zd, pos, current_plane.time, vvv1, vvv2, vvv3, vvv4, vvv5, vvv6, vvv7,jgtime)
													newpath=newjg[0]
													newchang=newjg[1]
													
								
													print(jcdian)
													print(vvv1)
													print(vvv3)
													print(current_plane.chang[index2])
									
													print(newpath)
													print(newchang)					
				
													newplane_dic[current_plane.index].path=newpath
													newplane_dic[current_plane.index].chang=newchang
													print(newplane_dic[current_plane.index].path)
													print(newplane_dic[current_plane.index].chang)
													newpri=current_plane.pri


													zzzzzz=1
													plane_queue.put((newpri, newplane_dic[current_plane.index]))

													break




												else:

													print('dddddd1')
													print(current_plane.index)
													print(close_airplane[index1].index)
													print(o0o)
													o0o += 1		
													print(newplane_dic[current_plane.index].path)
													print(newplane_dic[current_plane.index].chang)
													print(close_airplane[index1].path)
													print(close_airplane[index1].chang)


													jcdian=current_plane.path[index2]
													ooo=jgtime+abs(current_plane.chang[index2]-close_airplane[index1].chang[index3])
													www1=close_airplane[index1].index
													www2=close_airplane[index1].chang[index3]
													www3=2
													www4=ooo
													www5=close_airplane[index1].chang[index3 -1]
													www6=close_airplane[index1].path[index3 -1]
													
													newplane_dic[current_plane.index].chongtudian.append(jcdian)
													newplane_dic[current_plane.index].chongtuplane.append(www1)
													newplane_dic[current_plane.index].chongtuplanetime.append(www2)
													newplane_dic[current_plane.index].chongtuplanezhonglei.append(www3)
													newplane_dic[current_plane.index].chongtuwaittime.append(www4)
													newplane_dic[current_plane.index].chongtutime2.append(www5)
													newplane_dic[current_plane.index].chongtudian2.append(www6)


													vvv1=newplane_dic[current_plane.index].chongtudian
													vvv2=newplane_dic[current_plane.index].chongtuplane
													vvv3=newplane_dic[current_plane.index].chongtuplanetime
													vvv4=newplane_dic[current_plane.index].chongtuplanezhonglei
													vvv5=newplane_dic[current_plane.index].chongtuwaittime
													vvv6=newplane_dic[current_plane.index].chongtutime2
													vvv7=newplane_dic[current_plane.index].chongtudian2


													newjg=shortest_path1(airports, current_plane.qd, current_plane.zd, pos, current_plane.time, vvv1, vvv2, vvv3, vvv4, vvv5, vvv6, vvv7,jgtime)
													newpath=newjg[0]
													newchang=newjg[1]
													
								

													print(jcdian)
													print(ooo)
													print(vvv1)
													print(vvv3)
													
													print(vvv6)
													print(vvv7)
													print(current_plane.chang[index2])
									
													print(newpath)
													print(newchang)					
				
													newplane_dic[current_plane.index].path=newpath
													newplane_dic[current_plane.index].chang=newchang
													print(newplane_dic[current_plane.index].path)
													print(newplane_dic[current_plane.index].chang)
													newpri=current_plane.pri



													zzzzzz=1
													plane_queue.put((newpri, newplane_dic[current_plane.index]))

													break



										elif current_plane.chang[index2]-close_airplane[index1].chang[index3]<0  and  current_plane.chang[index2 +1]-close_airplane[index1].chang[index3 -1 ]>0  :




											if((index2 - 1)>=0 and (index3 +1)<len(close_airplane[index1].chang)):

												if current_plane.path[index2-1]==close_airplane[index1].path[index3 +1] and current_plane.path[index2-1] not in tinglist:


													print('ffffff3')
													print(current_plane.index)
													print(close_airplane[index1].index)
													print(o0o)
													o0o += 1		
													print(newplane_dic[current_plane.index].path)
													print(newplane_dic[current_plane.index].chang)
													print(close_airplane[index1].path)
													print(close_airplane[index1].chang)


													jcdian=current_plane.path[index2]
													ooo=100000
													www1=close_airplane[index1].index
													www2=close_airplane[index1].chang[index3]
													www3=3
													www4=ooo
													www5=close_airplane[index1].chang[index3 -1]
													www6=close_airplane[index1].path[index3 -1]
													
													newplane_dic[current_plane.index].chongtudian.append(jcdian)
													newplane_dic[current_plane.index].chongtuplane.append(www1)
													newplane_dic[current_plane.index].chongtuplanetime.append(www2)
													newplane_dic[current_plane.index].chongtuplanezhonglei.append(www3)
													newplane_dic[current_plane.index].chongtuwaittime.append(www4)
													newplane_dic[current_plane.index].chongtutime2.append(www5)
													newplane_dic[current_plane.index].chongtudian2.append(www6)


													vvv1=newplane_dic[current_plane.index].chongtudian
													vvv2=newplane_dic[current_plane.index].chongtuplane
													vvv3=newplane_dic[current_plane.index].chongtuplanetime
													vvv4=newplane_dic[current_plane.index].chongtuplanezhonglei
													vvv5=newplane_dic[current_plane.index].chongtuwaittime
													vvv6=newplane_dic[current_plane.index].chongtutime2
													vvv7=newplane_dic[current_plane.index].chongtudian2


													newjg=shortest_path1(airports, current_plane.qd, current_plane.zd, pos, current_plane.time, vvv1, vvv2, vvv3, vvv4, vvv5, vvv6, vvv7,jgtime)
													newpath=newjg[0]
													newchang=newjg[1]
													
								
													print(jcdian)
													print(vvv3)
													print(current_plane.chang[index2])
								
													print(vvv1)

													print(newpath)
													print(newchang)					
				
													newplane_dic[current_plane.index].path=newpath
													newplane_dic[current_plane.index].chang=newchang
													print(newplane_dic[current_plane.index].path)
													print(newplane_dic[current_plane.index].chang)
													newpri=current_plane.pri


													plane_queue.put((newpri, newplane_dic[current_plane.index]))
													zzzzzz=1
													break

												elif current_plane.path[index2-1]==close_airplane[index1].path[index3 +1]  and current_plane.path[index2 -1]  in tinglist:


													print('gggggg3')
													print(current_plane.index)
													print(close_airplane[index1].index)
													print(o0o)
													o0o += 1		
													print(newplane_dic[current_plane.index].path)
													print(newplane_dic[current_plane.index].chang)
													print(close_airplane[index1].path)
													print(close_airplane[index1].chang)

													while ((index2-1) >=0 and (index3 +1) < len(close_airplane[index1].path)): 


														if current_plane.path[index2 -1] == close_airplane[index1].path[index3 +1]:

															index2 -=1
															index3 +=1
															
														elif(current_plane.path[index2-1]!=close_airplane[index1].path[index3 +1]):

															break



													jcdian=current_plane.path[index2]
													ooo= jgtime +abs(close_airplane[index1].chang[index3] - current_plane.chang[index2])
													www1=close_airplane[index1].index
													www2=close_airplane[index1].chang[index3]
													www3=4
													www4=ooo
													www5=0
													www6=0
													
													newplane_dic[current_plane.index].chongtudian.append(jcdian)
													newplane_dic[current_plane.index].chongtuplane.append(www1)
													newplane_dic[current_plane.index].chongtuplanetime.append(www2)
													newplane_dic[current_plane.index].chongtuplanezhonglei.append(www3)
													newplane_dic[current_plane.index].chongtuwaittime.append(www4)
													newplane_dic[current_plane.index].chongtutime2.append(www5)
													newplane_dic[current_plane.index].chongtudian2.append(www6)


													vvv1=newplane_dic[current_plane.index].chongtudian
													vvv2=newplane_dic[current_plane.index].chongtuplane
													vvv3=newplane_dic[current_plane.index].chongtuplanetime
													vvv4=newplane_dic[current_plane.index].chongtuplanezhonglei
													vvv5=newplane_dic[current_plane.index].chongtuwaittime
													vvv6=newplane_dic[current_plane.index].chongtutime2
													vvv7=newplane_dic[current_plane.index].chongtudian2


													newjg=shortest_path1(airports, current_plane.qd, current_plane.zd, pos, current_plane.time, vvv1, vvv2, vvv3, vvv4, vvv5, vvv6, vvv7,jgtime)
													newpath=newjg[0]
													newchang=newjg[1]
													
								
													print(jcdian)
													print(vvv1)
													print(vvv3)
													print(current_plane.chang[index2])
									

													print(newpath)
													print(newchang)					
				
													newplane_dic[current_plane.index].path=newpath
													newplane_dic[current_plane.index].chang=newchang
													print(newplane_dic[current_plane.index].path)
													print(newplane_dic[current_plane.index].chang)
													newpri=current_plane.pri

													zzzzzz=1
													plane_queue.put((newpri, newplane_dic[current_plane.index]))

													break


												else:

													print('eeeeee1')
													print(current_plane.index)
													print(close_airplane[index1].index)
													print(o0o)
													o0o += 1
													print(newplane_dic[current_plane.index].path)
													print(newplane_dic[current_plane.index].chang)
													print(close_airplane[index1].path)
													print(close_airplane[index1].chang)


													jcdian=current_plane.path[index2]
													ooo=jgtime+abs(current_plane.chang[index2]-close_airplane[index1].chang[index3])
													www1=close_airplane[index1].index
													www2=close_airplane[index1].chang[index3]
													www3=2
													www4=ooo
													www5=close_airplane[index1].chang[index3 -1]
													www6=close_airplane[index1].path[index3 -1]
													
													newplane_dic[current_plane.index].chongtudian.append(jcdian)
													newplane_dic[current_plane.index].chongtuplane.append(www1)
													newplane_dic[current_plane.index].chongtuplanetime.append(www2)
													newplane_dic[current_plane.index].chongtuplanezhonglei.append(www3)
													newplane_dic[current_plane.index].chongtuwaittime.append(www4)
													newplane_dic[current_plane.index].chongtutime2.append(www5)
													newplane_dic[current_plane.index].chongtudian2.append(www6)


													vvv1=newplane_dic[current_plane.index].chongtudian
													vvv2=newplane_dic[current_plane.index].chongtuplane
													vvv3=newplane_dic[current_plane.index].chongtuplanetime
													vvv4=newplane_dic[current_plane.index].chongtuplanezhonglei
													vvv5=newplane_dic[current_plane.index].chongtuwaittime
													vvv6=newplane_dic[current_plane.index].chongtutime2
													vvv7=newplane_dic[current_plane.index].chongtudian2


													newjg=shortest_path1(airports, current_plane.qd, current_plane.zd, pos, current_plane.time, vvv1, vvv2, vvv3, vvv4, vvv5, vvv6, vvv7,jgtime)
													newpath=newjg[0]
													newchang=newjg[1]
													
								
													print(jcdian)
													print(vvv1)

													print(vvv3)
													print(current_plane.chang[index2])
									

													print(newpath)
													print(newchang)					
				
													newplane_dic[current_plane.index].path=newpath
													newplane_dic[current_plane.index].chang=newchang
													print(newplane_dic[current_plane.index].path)
													print(newplane_dic[current_plane.index].chang)
													newpri=current_plane.pri


													zzzzzz=1
													plane_queue.put((newpri, newplane_dic[current_plane.index]))

													break



			if (current_plane.index not in close_airplane) and (zzzzzz == 0):
				close_airplane.append(current_plane)


		elif  len(close_airplane)==0 :
			close_airplane.append(current_plane)
			print(current_plane.index)

	alltime=0
	numwaitnode=[]
	numall=0

	for index6 in range(len(waitplaneindex)):
		
		numnode=len(set(waitplane[waitplaneindex[index6]].waitplace))
		numwaitnode.append(numnode)
		numall += numnode
	
		for index7 in range(len(waitplane[waitplaneindex[index6]].waittime)):
			
			alltime += waitplane[waitplaneindex[index6]].waittime[index7]



	alltime2=0
	for index7 in range(len(planeindex)):
		dddd= max(newplane_dic[planeindex[index7]].chang)
		pppp= min(newplane_dic[planeindex[index7]].chang)

		oooo= dddd-pppp
		alltime2 += oooo

	numplane = len(waitplaneindex)

	jieguo3=[]
	jieguo3.append(newplane_dic)
	jieguo3.append(waitplaneindex)
	jieguo3.append(waitplane)
	jieguo3.append(alltime)
	jieguo3.append(alltime2)
	jieguo3.append(numplane)
	jieguo3.append(numwaitnode)
	jieguo3.append(numall)

	return jieguo3





with open('airplane.pickle', 'rb') as k:
	
	plane_dic=pickle.load(k)
	jinjiqingkuang=pickle.load(k)
	planeindex=pickle.load(k)
	pri=pickle.load(k)
	dian=pickle.load(k)
	zhongdian=pickle.load(k)
	zhong=pickle.load(k)
	tim=pickle.load(k)
	paths=pickle.load(k)
	lenths=pickle.load(k)


jgtime=10

jieguo2= bimianchongtu2(airports, pos, dian, zhongdian, zhong, tim, pri, planeindex, paths, lenths, jgtime)

newplane_dic2=jieguo2[0]
waitplaneindex2=jieguo2[1]
waitplane2=jieguo2[2]
alltime21=jieguo2[3]
alltime22=jieguo2[4]
numplane =jieguo2[5]
numwaitnode =jieguo2[6]
numall =jieguo2[7]

print('bbbbbb')
for index in range(len(planeindex)):
	print(newplane_dic2[planeindex[index]].index)
	print(newplane_dic2[planeindex[index]].zhong)
	print(newplane_dic2[planeindex[index]].qd)
	print(newplane_dic2[planeindex[index]].zd)
	print(newplane_dic2[planeindex[index]].time)
	print(newplane_dic2[planeindex[index]].path)
	print(newplane_dic2[planeindex[index]].chang)


print('aaaaaaaaaaa')
for index1 in range(len(waitplaneindex2)):
	print(waitplane2[waitplaneindex2[index1]].index)
	print(waitplane2[waitplaneindex2[index1]].waitplace)
	print(waitplane2[waitplaneindex2[index1]].timeofwait)
	print(waitplane2[waitplaneindex2[index1]].zhonglei)
	print(waitplane2[waitplaneindex2[index1]].waittime)
	print(numwaitnode[index1])



print(alltime21)

print(alltime22)


print(numplane)

print(numall)



