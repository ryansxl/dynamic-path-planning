import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import pickle
from queue import PriorityQueue as PQueue


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

jinjiqingkuang=0

nx.draw_networkx_nodes(airports,pdpos,pdlist,node_size=10,node_color='k',with_labels=True)
nx.draw_networkx_nodes(airports,hxpos,hxlist,node_size=10,node_color='k',with_labels=True)
nx.draw_networkx_nodes(airports,tjpos,tjlist,node_size=15,node_color='k',with_labels=True)

nx.draw_networkx_edges(airports,pos,pedges,width=5.0,edge_color='k')
nx.draw_networkx_edges(airports,pos,hedges,width=1.0,edge_color='k')
nx.draw_networkx_edges(airports,pos,ledges,width=1.0,edge_color='k')

plt.show()

with open('airport.pickle', 'wb') as f:
	pickle.dump(airports, f, pickle.HIGHEST_PROTOCOL)
	pickle.dump(pos, f, pickle.HIGHEST_PROTOCOL)	
	pickle.dump(pdpos, f, pickle.HIGHEST_PROTOCOL)	
	pickle.dump(hxpos, f, pickle.HIGHEST_PROTOCOL)	
	pickle.dump(tjpos, f, pickle.HIGHEST_PROTOCOL)	
	pickle.dump(pdlist, f, pickle.HIGHEST_PROTOCOL)	
	pickle.dump(hxlist, f, pickle.HIGHEST_PROTOCOL)	
	pickle.dump(tjlist, f, pickle.HIGHEST_PROTOCOL)	
	pickle.dump(pedges, f, pickle.HIGHEST_PROTOCOL)	
	pickle.dump(hedges, f, pickle.HIGHEST_PROTOCOL)	
	pickle.dump(ledges, f, pickle.HIGHEST_PROTOCOL)	




