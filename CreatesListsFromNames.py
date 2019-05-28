# -*- coding: utf-8 -*-
"""
Created on Sat Apr 20 17:18:01 2019

@author: ROHAN
"""
l=[]
with open('new.txt','r') as f:
    m = f.readlines()
   #l.append(m.strip())

new=[]   
for k in m:
    k = k.replace('\n','')
    
    new.append(k)
    new

lists = [new[x:x+129] for x in range(0, len(new),129)]
with open('list.txt', 'a') as o:
    o.write('[')
    for i in lists:
        o.write('[')
        for n in i:
            
            o.write('"')
            o.write(n)
            o.write('"')
            o.write(',')
        o.write(']')    
        o.write('\n')
    o.write(']')      
