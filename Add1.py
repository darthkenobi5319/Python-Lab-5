# -*- coding: utf-8 -*-
"""
Created on Tue Sep 19 11:43:47 2017

@author: ZHENGHAN ZHANG
"""
#randomize the list
import random
x=[]

for i in range(random.randrange(1,11)):
    y=[]
    for j in range(random.randrange(1,11)):
        y.append(random.randrange(1,11))
    x.append(y)
    
print(x)



#define the list and numerators
#x = [[1, 2], [3], [4, 5, 6, 7], [8, 9]]
#initialize the parameters
m=0
n=0
q=0
#Count the number of even values in the list
while m<len(x):
    n=0
    while n<len(x[m]):
        if x[m][n]%2==0:
            q+=1
        n+=1
    m+=1
print(q)

#Count the number of odd values contained in sublists with more than two elements  
#reset the parameters
q=0      
m=0
while m<len(x):
    n=0
    while n<len(x[m]) and len(x[m])>2:
        if x[m][n]%2!=0:
            q+=1
        n+=1
    m+=1
print(q)