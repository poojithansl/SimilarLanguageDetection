#!/usr/bin/env python
# -*- coding: utf-8 -*-
import string
f=open('train.txt',mode='r')
df=open('preproctrain.txt',mode='w')
#t=f.readlines()
for line in f:
    out_line = line.translate(string.maketrans("",""),string.digits+string.punctuation)
    df.write(out_line)

f.close()
df.close()
