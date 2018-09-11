# -*- coding: utf-8 -*-
"""
Created on Tue Sep 19 10:29:34 2017

@author: ZHENGHAN ZHANG
"""

for i in range(1,101):
    if (i%3)==0 and (i%5)!=0:
        print('Fizz')
    elif (i%3)!=0 and (i%5)==0:
        print('Buzz')
    elif (i%3)==0 and (i%5)==0:
        print('FizzBuzz')
    else:
        print(i)
        