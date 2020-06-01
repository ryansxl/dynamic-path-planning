import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import pickle

airports=nx.Graph()

wnlist=['w1','w2','w3','w4','w5','w6','w7','w8','w9','w10','w11']
for i in range(0,11):
        airports.add_node(wnlist[i])

rnlist=['r1','r2','r3','r4','r5','r6','r7','r8','r9','r10','r11','r12','r13']
for i in range(0,13) :
        airports.add_node(rnlist[i])

qnlist=['q1','q2','q3','q4','q5','q6','q7','q8','q9','q10','q11','q12']
for i in range(0,12) :
        airports.add_node(qnlist[i])

aanlist=['m','n','r','s','t','u','v','w','x','y','z','z1','z2','z3','z4','z5']
for i in range(0,16) :
        airports.add_node(aanlist[i])

bbnlist=['l','k','j','i','h','g','f','e','c','b','a']
for i in range(0,11) :
        airports.add_node(bbnlist[i])

anlist=['a0','a1','a2','a3','a4','a5','a6','a7','a8','a9','a10']
for i in range(0,11) :
        airports.add_node(anlist[i])

atnlist=[101,102,103,104,105,106,107,108,109,110,111]
for i in range(0,11) :
        airports.add_node(atnlist[i])

bnlist=['b0','b1','b2','b3','b4','b5','b6']
for i in range(0,7) :
        airports.add_node(bnlist[i])

btnlist=[201,202,203,204,205,206,207]
for i in range(0,7) :
        airports.add_node(btnlist[i])

cnlist=['c0','c1','c2','c3','c4','c5']
for i in range(0,6) :
        airports.add_node(cnlist[i])

ctnlist=[301,302,303,304,305,306]
for i in range(0,6) :
        airports.add_node(ctnlist[i])

fnlist=['f0','f1','f2','f3']
for i in range(0,4) :
        airports.add_node(fnlist[i])

ftnlist=[401,402,403,404]
for i in range(0,4) :
        airports.add_node(ftnlist[i])

gnlist=['g0','g1','g2','g3','g4','g5','g6','g7']
for i in range(0,8) :
        airports.add_node(gnlist[i])

gtnlist=[501,502,503,504,505,506,507,508]
for i in range(0,8) :
        airports.add_node(gtnlist[i])

hnlist=['h0','h1','h2','h3','h4','h5','h6','h7']
for i in range(0,8) :
        airports.add_node(hnlist[i])

htnlist=[601,602,603,604,605,606,607,608]
for i in range(0,8) :
        airports.add_node(htnlist[i])

inlist=['i0','i1','i2','i3','i4','i5','i6','i7','i8']
for i in range(0,9) :
        airports.add_node(inlist[i])

itnlist=[701,702,703,704,705,706,707,708,709]
for i in range(0,9) :
        airports.add_node(itnlist[i])

jnlist=['j0','j1','j2','j3','j4']
for i in range(0,5) :
        airports.add_node(jnlist[i])

jtnlist=[801,802,803,804,805]
for i in range(0,5) :
        airports.add_node(jtnlist[i])

knlist=['k0','k1','k2','k3','k4','k5','k6']
for i in range(0,7) :
        airports.add_node(knlist[i])

ktnlist=[901,902,903,904,905,906,907]
for i in range(0,7) :
        airports.add_node(ktnlist[i])

pdlist=wnlist+rnlist

hxlist=qnlist+aanlist+bbnlist+anlist+bnlist+cnlist+fnlist+gnlist+hnlist+inlist+jnlist+knlist

tjlist=atnlist+btnlist+ctnlist+ftnlist+gtnlist+htnlist+itnlist+jtnlist+ktnlist

pointlist = pdlist + hxlist + tjlist

pedges = [['w1','w2'],['w2','w3'],['w3','w4'],['w4','w5'],['w5','w6'],['w6','w7'],['w7','w8'],['w8','w9'],['w9','w10'],['w10','w11'],
          ['r1','r2'],['r2','r3'],['r3','r4'],['r4','r5'],['r5','r6'],['r6','r7'],['r7','r8'],['r8','r9'],['r9','r10'],['r10','r11'],['r11','r12'],['r12','r13']]

hedges=[  ['q1','q2'],['q2','q3'],['q3','q4'],['q4','q5'],['q5','q6'],['q6','q7'],['q7','q8'],['q8','q9'],['q9','q10'],['q10','q11'],['q11','q12'],
        ['m','n'],['n','r'],['r','s'],['s','t'],['t','u'],['u','v'],['v','w'],['w','x'],['x','y'],['y','z'],['z','z1'],['z1','z2'],['z2','z3'],['z3','z4'],['z4','z5'],
        ['l','k'],['k','j'],['j','i'],['i','h'],['h','g'],['g','f'],['f','e'],['e','c'],['c','b'],['b','a']]

ledges=[['w11','q12'],['w10','q11'],['w9','q9'],['w8','q8'],['w8','q7'],['w7','q7'],['w7','q6'],['w6','q5'],['w5','q4'],['w4','q4'],['w3','q3'],['w2','q2'],['w1','q1'],
             ['q1','r1'],['q2','r4'],['q3','r4'],['q3','r5'],['q4','r5'],['q4','r6'],['q5','r6'],['q6','r7'],['q7','r8'],['q7','r9'],['q8','r10'],['q8','r11'],['q10','r13'],
             ['r1','z5'],['r2','z4'],['r3','z3'],['r3','z2'],['r4','z1'],['r5','z'],['r6','y'],['r8','v'],['r9','u'],['r10','s'],['r11','r'],['r12','n'],['r13','m'],
             ['z1','a'],['y','b'],['x','c'],['w','e'],['v','f'],['u','g'],['t','h'],['s','i'],['r','j'],['n','k'],['m','l'],

             ['a','a0'],['a0','a1'],['a1','a2'],['a2','a3'],['a3','a4'],['a4','a5'],['a5','a6'],['a6','a7'],['a7','a8'],['a8','a9'],['a9','a10'],
             ['a0',101],['a1',102],['a2',103],['a3',104],['a4',105],['a5',106],['a6',107],['a7',108],['a8',109],['a9',110],['a10',111],

             ['b','b0'],['b0','b1'],['b1','b2'],['b2','b3'],['b3','b4'],['b4','b5'],['b5','b6'],
             ['b0',201],['b1',202],['b2',203],['b3',204],['b4',205],['b5',206],['b6',207],

             ['c','c0'],['c0','c1'],['c1','c2'],['c2','c3'],['c3','c4'],['c4','c5'],
             ['c0',301],['c1',302],['c2',303],['c3',304],['c4',305],['c5',306],

             ['f','f0'],['f0','f1'],['f1','f2'],['f2','f3'],
             ['f0',401],['f1',402],['f2',403],['f3',404],

             ['g','g0'],['g0','g1'],['g1','g2'],['g2','g3'],['g3','g4'],['g4','g5'],['g5','g6'],['g6','g7'],
             ['g0',501],['g1',502],['g2',503],['g3',504],['g4',505],['g5',506],['g6',507],['g7',508],

             ['h','h0'],['h0','h1'],['h1','h2'],['h2','h3'],['h3','h4'],['h4','h5'],['h5','h6'],['h6','h7'],
             ['h0',601],['h1',602],['h2',603],['h3',604],['h4',605],['h5',606],['h6',607],['h7',608],

             ['i','i0'],['i0','i1'],['i1','i2'],['i2','i3'],['i3','i4'],['i4','i5'],['i5','i6'],['i6','i7'],['i7','i8'],
             ['i0',701],['i1',702],['i2',703],['i3',704],['i4',705],['i5',706],['i6',707],['i7',708],['i8',709],

             ['j','j0'],['j0','j1'],['j1','j2'],['j2','j3'],['j3','j4'],
             ['j0',801],['j1',802],['j2',803],['j3',804],['j4',805],

             ['k','k0'],['k0','k1'],['k1','k2'],['k2','k3'],['k3','k4'],['k4','k5'],['k5','k6'],
             ['k0',901],['k1',902],['k2',903],['k3',904],['k4',905],['k5',906],['k6',907] ]

edges=pedges+hedges+ledges

airports.add_edges_from(edges)

#nx.draw(airports)
#plt.show()

wnodes=np.loadtxt('w.txt',dtype=np.int32)
rnodes=np.loadtxt('r.txt',dtype=np.int32)
qnodes=np.loadtxt('q.txt',dtype=np.int32)
aanodes=np.loadtxt('aa.txt',dtype=np.int32)
bbnodes=np.loadtxt('bb.txt',dtype=np.int32)
anodes=np.loadtxt('a.txt',dtype=np.int32)
atnodes=np.loadtxt('at.txt',dtype=np.int32)
bnodes=np.loadtxt('b.txt',dtype=np.int32)
btnodes=np.loadtxt('bt.txt',dtype=np.int32)
cnodes=np.loadtxt('c.txt',dtype=np.int32)
ctnodes=np.loadtxt('ct.txt',dtype=np.int32)
fnodes=np.loadtxt('f.txt',dtype=np.int32)
ftnodes=np.loadtxt('ft.txt',dtype=np.int32)
gnodes=np.loadtxt('g.txt',dtype=np.int32)
gtnodes=np.loadtxt('gt.txt',dtype=np.int32)
hnodes=np.loadtxt('h.txt',dtype=np.int32)
htnodes=np.loadtxt('ht.txt',dtype=np.int32)
inodes=np.loadtxt('i.txt',dtype=np.int32)
itnodes=np.loadtxt('it.txt',dtype=np.int32)
jnodes=np.loadtxt('j.txt',dtype=np.int32)
jtnodes=np.loadtxt('jt.txt',dtype=np.int32)
knodes=np.loadtxt('k.txt',dtype=np.int32)
ktnodes=np.loadtxt('kt.txt',dtype=np.int32)


wpos=dict(zip(wnlist,wnodes))
rpos=dict(zip(rnlist,rnodes))
qpos=dict(zip(qnlist,qnodes))
aapos=dict(zip(aanlist,aanodes))
bbpos=dict(zip(bbnlist,bbnodes))
apos=dict(zip(anlist,anodes))
atpos=dict(zip(atnlist,atnodes))
bpos=dict(zip(bnlist,bnodes))
btpos=dict(zip(btnlist,btnodes))
cpos=dict(zip(cnlist,cnodes))
ctpos=dict(zip(ctnlist,ctnodes))
fpos=dict(zip(fnlist,fnodes))
ftpos=dict(zip(ftnlist,ftnodes))
gpos=dict(zip(gnlist,gnodes))
gtpos=dict(zip(gtnlist,gtnodes))
hpos=dict(zip(hnlist,hnodes))
htpos=dict(zip(htnlist,htnodes))
ipos=dict(zip(inlist,inodes))
itpos=dict(zip(itnlist,itnodes))
jpos=dict(zip(jnlist,jnodes))
jtpos=dict(zip(jtnlist,jtnodes))
kpos=dict(zip(knlist,knodes))
ktpos=dict(zip(ktnlist,ktnodes))

pdpos={}
pdpos=wpos.copy()
pdpos.update(rpos)

hxpos={}
hxpos=apos.copy()
hxpos.update(qpos)
hxpos.update(aapos)
hxpos.update(bbpos)
hxpos.update(apos)
hxpos.update(bpos)
hxpos.update(cpos)
hxpos.update(fpos)
hxpos.update(gpos)
hxpos.update(hpos)
hxpos.update(ipos)
hxpos.update(jpos)
hxpos.update(kpos)

tjpos={}
tjpos=atpos.copy()
tjpos.update(btpos)
tjpos.update(ctpos)
tjpos.update(ftpos)
tjpos.update(gtpos)
tjpos.update(htpos)
tjpos.update(itpos)
tjpos.update(jtpos)
tjpos.update(ktpos)

pos={}
pos=pdpos.copy()
pos.update(hxpos)
pos.update(tjpos)


nx.draw_networkx_nodes(airports,pdpos,pdlist,node_size=10,node_color='k',with_labels=True)
nx.draw_networkx_nodes(airports,hxpos,hxlist,node_size=10,node_color='k',with_labels=True)
nx.draw_networkx_nodes(airports,tjpos,tjlist,node_size=15,node_color='k',with_labels=True)

nx.draw_networkx_edges(airports,pos,pedges,width=5.0,edge_color='k')
nx.draw_networkx_edges(airports,pos,hedges,width=1.0,edge_color='k')
nx.draw_networkx_edges(airports,pos,ledges,width=1.0,edge_color='k')

from showp import showpath, showdian
from jingtai1 import node, cal_dist, shortest_path, find_path



ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.spines['left'].set_color('none')
ax.spines['bottom'].set_color('none')
plt.xticks(())
plt.yticks(())

tim=[0,300,105,200,0,400,300,250,25,500]
chang1=[]
path1= shortest_path(airports, 'w1', 601, pos)
lenth1=0
chang1.append(lenth1)
for index in range (len(path1)-1) : 
		mmm=cal_dist(path1[index] , path1[index+1] , pos)
		lenth1=lenth1+mmm
		chang1.append(lenth1)


chang2=[]
path2= shortest_path(airports, 202, 'r1', pos)
lenth2=300
chang2.append(lenth2)
for index in range (len(path2)-1) : 
		mmm=cal_dist(path2[index] , path2[index+1] , pos)
		lenth2=lenth2+mmm
		chang2.append(lenth2)


chang3=[]
path3= shortest_path(airports, 901, 'r1', pos)
lenth3=105
chang3.append(lenth3)
for index in range (len(path3)-1) : 
		mmm=cal_dist(path3[index] , path3[index+1] , pos)
		lenth3=lenth3+mmm
		chang3.append(lenth3)


chang4=[]
path4= shortest_path(airports, 'w1', 702, pos)
lenth4=200
chang4.append(lenth4)
for index in range (len(path4)-1) : 
		mmm=cal_dist(path4[index] , path4[index+1] , pos)
		lenth4=lenth4+mmm
		chang4.append(lenth4)


chang5=[]
path5= shortest_path(airports, 504, 'r1', pos)
lenth5=0
chang5.append(lenth5)
for index in range (len(path5)-1) : 
		mmm=cal_dist(path5[index] , path5[index+1] , pos)
		lenth5=lenth5+mmm
		chang5.append(lenth5)

chang6=[]
path6= shortest_path(airports, 'w1', 703, pos)
lenth6=400
chang6.append(lenth6)
for index in range (len(path6)-1) : 
		mmm=cal_dist(path6[index] , path6[index+1] , pos)
		lenth6=lenth6+mmm
		chang6.append(lenth6)

chang7=[]
path7= shortest_path(airports, 501, 'r1', pos)
lenth7=300
chang7.append(lenth7)
for index in range (len(path7)-1) : 
		mmm=cal_dist(path7[index] , path7[index+1] , pos)
		lenth7=lenth7+mmm
		chang7.append(lenth7)

chang8=[]
path8= shortest_path(airports, 502, 'r1', pos)
lenth8=250
chang8.append(lenth8)
for index in range (len(path8)-1) : 
		mmm=cal_dist(path8[index] , path8[index+1] , pos)
		lenth8=lenth8+mmm
		chang8.append(lenth8)


chang9=[]
path9= shortest_path(airports, 'w1', 602, pos)
lenth9=25
chang9.append(lenth9)
for index in range (len(path9)-1) : 
		mmm=cal_dist(path9[index] , path9[index+1] , pos)
		lenth9=lenth9+mmm
		chang9.append(lenth9)


chang10=[]
path10= shortest_path(airports, 'w1', 401, pos)
lenth10=500
chang10.append(lenth10)
for index in range (len(path10)-1) : 
		mmm=cal_dist(path10[index] , path10[index+1] , pos)
		lenth10=lenth10+mmm
		chang10.append(lenth10)








paths=[path1, path2, path3, path4, path5, path6, path7, path8, path9,path10]
lenths=[chang1,chang2, chang3, chang4, chang5, chang6, chang7 ,chang8, chang9 ,chang10]
print(paths)
print(lenths)

color=['#FF0000', '#0000CD', '#00688B', '#FF34B3', '#00EEEE', '#FF6347', '#00FF7F', '#00C5CD', '#FFBBFF', '#FFAEB9']


#color=['#00688B','#FFBBFF']

plt.text(-45, 140, 'airplane:CA405', color=color[0])
plt.text(-45, 135, 'airplane:3U8849', color=color[1])
plt.text(-45, 130, 'airplane:CZ3183', color=color[2])
plt.text(-45, 125, 'airplane:PN6237', color=color[4])
plt.text(-45, 120, 'airplane:3U8741', color=color[6])
plt.text(-45, 115, 'airplane:CA2158', color=color[7])


plt.text(-45, 110, 'airplane:CA1419', color=color[3])
plt.text(-45, 105, 'airplane:3U8935', color=color[5])
plt.text(-45, 100, 'airplane:3U8633', color=color[8])
plt.text(-45, 95, 'airplane:CA4123', color=color[9])

dian=['w1',202,901,'w1',504,'w1',501,502,'w1','w1']
zhongdian=[601,'r1','r1',702,'r1',703,'r1',703,'r1','r1',602,401]
zhong=[1,0,0,1,0,1,0,0,1,1]
tim=[0,300,105,200,0,400,300,250,25,500]
from showp import showdian,showpath
v=10
t00=0

while t00<700 :
	nx.draw_networkx_nodes(airports,pdpos,pdlist,node_size=10,node_color='k',with_labels=True)
	nx.draw_networkx_nodes(airports,hxpos,hxlist,node_size=10,node_color='k',with_labels=True)
	nx.draw_networkx_nodes(airports,tjpos,tjlist,node_size=15,node_color='k',with_labels=True)

	nx.draw_networkx_edges(airports,pos,pedges,width=5.0,edge_color='k')
	nx.draw_networkx_edges(airports,pos,hedges,width=1.0,edge_color='k')
	nx.draw_networkx_edges(airports,pos,ledges,width=1.0,edge_color='k')

	
	ax = plt.gca()
	ax.spines['right'].set_color('none')
	ax.spines['top'].set_color('none')
	ax.spines['left'].set_color('none')
	ax.spines['bottom'].set_color('none')
	plt.xticks(())
	plt.yticks(())

	plt.text(-45, 140, 'airplane:CA405', color=color[0])
	plt.text(-45, 135, 'airplane:3U8849', color=color[1])
	plt.text(-45, 130, 'airplane:CZ3183', color=color[2])
	plt.text(-45, 125, 'airplane:PN6237', color=color[4])
	plt.text(-45, 120, 'airplane:3U8741', color=color[6])
	plt.text(-45, 115, 'airplane:CA2158', color=color[7])


	plt.text(-45, 110, 'airplane:CA1419', color=color[3])
	plt.text(-45, 105, 'airplane:3U8935', color=color[5])
	plt.text(-45, 100, 'airplane:3U8633', color=color[8])
	plt.text(-45, 95, 'airplane:CA4123', color=color[9])


	for index2 in range( len(tim) ) :
		maxchang = max(lenths[index2])
		if  ( zhong[index2] ==0 ) and ( tim[index2] >= t00 ) :
			showdian (airports, dian[index2] , pos, color[index2])
		if  (maxchang<=t00)  and  (zhong[index2] ==1) :
			showdian (airports, zhongdian[index2] , pos, color[index2])
		if   tim[index2] == t00 :
			showdian (airports, dian[index2] , pos, color[index2])
		if  (tim[index2] < t00) and  (maxchang>=t00) :
			pathii=[]
			for index3 in range ( len(lenths[index2]) ) :
				pathii.append(  paths[index2][index3]  )
				if  lenths[index2][index3] == t00 :
					showpath(airports, pathii, pos, color[index2])
				elif  (lenths[index2][index3] < t00) and (lenths[index2][index3+1] > t00) :
					ppp1=lenths[index2][index3+1]-lenths[index2][index3]
					ppp2=t00-lenths[index2][index3]
					x111=pos [ paths[index2][index3] ][0]
					y111=pos [ paths[index2][index3] ][1]
					x222=pos [ paths[index2][index3 + 1] ][0]
					y222=pos [ paths[index2][index3 + 1] ][1]
					x333= (x222-x111)*ppp2/ppp1+x111
					y333= (y222-y111)*ppp2/ppp1+y111					
					x444= int (x333)
					y444= int (y333)
					
					airports.add_node( index2 )
					airports.add_edge( paths[index2][index3] , index2)
					newpos={ index2 : [x444,y444] }
					pos.update(newpos)
					
					nowairplaneedge = [ ] 
					for index4 in range ( len(pathii)-1 ) :
						nowairplaneedge.append( [pathii[index4] , pathii[index4+1] ] )
					nowairplaneedge.append([ pathii[index3] , index2 ] )
					nx.draw_networkx_edges(airports, pos, nowairplaneedge, width=1.0, edge_color=color[index2])


					nowairplanepos={}
					for i in pathii :
						nowairplanepos.update( { i : pos[i] } )
					nowairplanepos.update(newpos)
					pathii.append( index2 )
					nx.draw_networkx_nodes (airports, nowairplanepos, pathii, node_size=25, node_color=color[index2],with_labels=True)
					print(pathii)

		
	plt.text(115, -25 , 'time = %d  s'%t00, color='k')
	print(t00)
	kkk=t00/10
	plt.savefig("%d.jpg"%kkk)
	plt.close()
	t00=t00+10

plt.show()
