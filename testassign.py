# -*- coding: utf-8 -*-
"""
Created on Tue Aug 22 15:05:08 2023

@author: urmii
"""

l1=[1,2,3,2,3,4,3,4,4,3,3,4,7]
def search(n):
    for i in l1:
        if n==i:
            print(i)
n=int(input("Enter a number"))
search(n)

l1=[1,2,3,2,3,4,3,4,4,3,3,4,7]
l2=[]
l3=[]
for i in l1:
    if i not in l2:
        l2.append(i)
        
    else:
        l3.append(i)
#print(l2)
print(l3)

l1=[2,3,4,5,1,2,3,4]
l2=[i+6 for i in l1]
print(l2)

s1='Hello'
s1[::-1]

d1={'x':1,'y':12,'z':3}
for i in d1:
    print(i,':',d1[i],end=' ')

d1={'x':1000,'y':1200,'z':3000,'a':2500}
d2={key:value for (key,value) in d1.items() if value>2000}
print(d2)

f='pi_digits.txt'
with open(f,'r') as file:
    for line in file:
        content=line.strip()
        print(content)

l1=[1,2,3,4,5,6,7,8,9,10]
even=[]
odd=[]
x =lambda x:x%2==0
#print(x)
for i in l1:
    if x(i):
        even.append(i)
    else:
        odd.append(i)
print(even)
print(odd)


x =lambda x:x%2==0
l1=[1,2,3,4,5,6,7,8,9,10]
x(l1)

import pandas as pd
import numpy as np
d1={'name':['anna','dinu','ramu','ganu','emily','mahesh','jayesh','venkat','ajay','dhanesh']
    ,
    'score':[12.5,16.5,np.nan,9,20,14.5,np.nan,8,19,12],
    'attempts':[1,2,3,4,5,6,7,8,9,10],
    'qualify':['yes','yes','no','yes','yes','no','yes','no','yes','no']
    }
d2=pd.DataFrame(d1)
print(d2)   
labels=['a','b','d','e','f','g','h','i','j','k']
d1=pd.DataFrame(d1,index=labels)
d1

#write a python program to plot two or more lines and set the line markers

dic = {'x':1,
        'y':34,
        'e':3
        }
l = [i for i in dic.values()]
l.sort()
l
k = [(i,j) for i,j in dic.items()]
print(k)
def last(n):
    return n[-1]
k = sorted(k,key=last)
k
dic_res = dict(k)
dic_res

#write python prog to construct the infinite iterator that returns the evenly spaced value values 
#starting with the specified no. and steps

import itertools
start_n = 10
steps = 100
counter = itertools.count(start=start_n,step=steps)
for i in counter:
    print(i)


#write a python prog to plot two or more lines and set the line markers

import matplotlib.pyplot as plt

import numpy as np
x = [1,2,3,4,5]
plt.plot([xi**2 for xi in x ],'o')
plt.plot([xi*2 for xi in x],'--')
plt.plot([xi+3 for xi in x],':')
plt.show()


