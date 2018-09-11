# -*- coding: utf-8 -*-
"""
Created on Tue Sep 19 10:01:52 2017

@author: ZHENGHAN ZHANG
"""

x = 3
if x < 2:
  print('a')
else:
  if x < 4:
    print('b')
  else:
    if x < 6:
      print('c')
    else:
      print('d')
print(x)


if x < 2:
    print('a')
elif x < 4:
    print('b')
elif x < 6:
    print('c')
else:
      print('d')
print(x)