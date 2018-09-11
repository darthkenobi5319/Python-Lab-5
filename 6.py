# -*- coding: utf-8 -*-
"""
Created on Tue Sep 19 11:14:33 2017

@author: ZHENGHAN ZHANG
"""

#Enter your friends name, or 'stop' to finish:

listName=[]
while True:
    x = input("Enter your friends name, or 'stop' to finish: ")
    if x == 'stop':
        break
    listName.append(x)
print('You have',len(listName),'friends',"They're: ")
for i in range(len(listName)-2):    
    print(listName[i],',',sep='')
print(listName[-2],', and',sep='')
print(listName[-1])
    
