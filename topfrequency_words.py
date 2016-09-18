#!/usr/bin/env python
# -*- coding: utf-8 -*-
import operator
import codecs
f = codecs.open('train_small.txt',encoding='utf-8')
fl = f.read().splitlines()
#print "".join(fl).encode('utf-8')
E={}
F={}
BG={}
MK={}
BS={}
HR={}
SR={}
CZ={}
SK={}
AR={}
ES={}
BR={}
ID={}
PT={}
MY={}
xx={}
tot=0
cnt=0
die={'bg':BG, 'mk':MK, 'bs':BS, 'hr':HR, 'sr':SR, 'cz':CZ, 'sk':SK, 'es-AR':AR, 'es-ES':ES, 'pt-BR':BR ,'pt-PT':PT,'id':ID, 'my':MY ,'xx':xx}
D={}
for i in range(len(fl)):
	fw = fl[i].split()
	tot+=1
	#fw=str(fw).decode('utf-8')
	if fw[-1].encode('utf-8') not in die.keys():
		cnt+=1
		print fl[i].encode('utf-8')
		print i
	else:
		d=die[fw[-1].encode('utf-8')]

	for j in range(len(fw)-1):
		
		#print fw[j].encode('utf-8')
		if fw[j] in d:
			d[fw[j].encode('utf-8')] += 1
		else:
			d[fw[j].encode('utf-8')] = 1
print cnt,tot
top_words={}
temp=[]
for i in die.keys():
	temp=[]
	#print die[i]
	g = sorted(die[i].items(), key=operator.itemgetter(1))
	g.reverse()
	#print g
	t=0
	for j in g:
	 	if t<1000:
	 		temp.append(j[0])
	 	else:
	 		break
	 	t+=1
	top_words[i]=temp

print top_words
