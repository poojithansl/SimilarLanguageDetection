#!/usr/bin/env python
# -*- coding: utf-8 -*-
import string
#f=open('train.txt',mode='r')
f=open('preproctrain.txt',mode='r')
df=open('preproctrainreal.txt',mode='w')
#t=f.readlines()
"""
for line in f:
    oline = line.translate(string.maketrans("",""),string.digits+string.punctuation)
    df.write(oline)

df.close()
"""
for line in f:
	oline = line.decode('utf-8').lower()
	df.write(oline.encode('utf-8'))
	#print out_line
df.close()
f.close()
