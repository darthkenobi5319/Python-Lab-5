# -*- coding: utf-8 -*-
"""
Created on Tue Sep 19 21:26:35 2017

@author: ZHENGHAN ZHANG
"""

#Single character, multiple casing
#with user input

source = input('Your string: ')
s1 = input('Unwanted character: ')
s2 = input('Replacement character: ')

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