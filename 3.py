# -*- coding: utf-8 -*-
"""
Created on Tue Sep 19 10:41:31 2017

@author: ZHENGHAN ZHANG
"""
#define the list and numerators
x = [[1, 2], [3], [4, 5, 6, 7], [8, 9]]
m=0
n=0

#Count the number of even values in the list
for i in range(len(x)):
    for j in range(len(x[i])):
        m+=int(x[i][j]%2==0)
print(m)

#Count the number of odd values contained in sublists with more than two elements

for i in range(len(x)):
    for j in range(len(x[i])):
        if len(x[i])>2:
            n+=int(x[i][j]%2!=0)
print(n)