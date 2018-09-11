# -*- coding: utf-8 -*-
"""
Created on Tue Sep 19 10:48:56 2017

@author: ZHENGHAN ZHANG
"""

#define the string
x = 'When the saints go marching in'

#reverse using the for loop
m=''
for i in range(len(x)):
    m+=x[-(i+1)]
print(m)

#reverse using the while loop
i=1
n=''
while i<=len(x):
    n+=x[-i]
    i+=1
print(n)