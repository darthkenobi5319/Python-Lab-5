# -*- coding: utf-8 -*-
"""
Created on Tue Sep 19 21:29:22 2017

@author: ZHENGHAN ZHANG
"""

#Multiple character, multiple casing, user input

source = input('Your string: ')
s1 = input('Unwanted character(s): ')
s2 = input('Replacement character: ')

# insert code here to create target
for i in s1:
#re-initialize the parameters
    target=''
    for j in source:
        if j == i:
            target += s2
        elif i == j.lower():
            target += s2.upper()
        else:
            target += j
    source=target
print(target)