# -*- coding: utf-8 -*-
"""
Created on Tue Sep 19 21:22:37 2017

@author: ZHENGHAN ZHANG
"""

#Single character, multiple casing
#use the provided skeleton code
source = 'Adam made him take a placard'
s1 = 'a'
s2 = 'z'

# insert code here to create target
#initialize the parameters
target=''
for i in source:
    if s1 == i:
        target += s2
    elif s1 == i.lower():
        target += s2.upper()
    else:
        target += i        
print(target)

 # should produce 'Zdzm mzde him tzke z plzczrd'