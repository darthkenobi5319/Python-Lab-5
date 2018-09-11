# -*- coding: utf-8 -*-
"""
Created on Tue Sep 19 21:16:30 2017

@author: ZHENGHAN ZHANG
"""

#single character, single casing
#directly use the skeleton code

source = 'Adam made him take a placard'
s1 = 'a'
s2 = 'z'


# insert code here to create target
target=''
for i in source:
    if s1 == i:
        target += s2
    else:
        target += i        
print(target)


 # should produce 'Adzm mzde him tzke z plzczrd'