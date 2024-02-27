# -*- coding: utf-8 -*-
"""
Created on Tue Aug  1 14:42:00 2023

@author: urmii
"""
#shallow and deep copies
l1=[1,2,3,4,5]
l2=l1
l2[0]=-10
print(l2)
print(l1)
########################################################
#shallow copy
#one level shallow deep which is not affect other list
import copy
l1=[1,2,3,4,5]
l2=copy.copy(l1)
l2[0]=-10
print(l2)
print(l1)
#two level shallow copies which affect other list as well
l1=[[3,4,5,6],[12,3,4,5]]
l2=l1
l2[1][0]=-10
print(l2)
print(l1)

#deep copies
#full independent clones are created
#to create deep copy we need to used deepcopy() of copy module
import copy
l1=[[3,4,5,6],[12,3,4,5]]
l2=copy.deepcopy(l1)
l2[0][0]=-10
print(l2)
print(l1)
####################################################
#write a python program to create an iterator 
#frm several iterables in a sequance and display
#the type of element of the new iterator
from itertools import chain
def chain_fun(l1,l2,l3):
    return chain(l1,l2,l3)
result=chain_fun([1,2,3,4], ['a','b','c','d'], [1,2,3,4,1,2,3,4,4])
print(type(result))   #<class 'itertools.chain'>
for i in result:
    print(i)

#tuple
from itertools import chain
def chain_fun(l1,l2,l3):
    return chain(l1,l2,l3)
result=chain_fun((1,2,3,4), ('a','b','c','d'), (1,2,3,4,1,2,3,4,4))
print(type(result))   #<class 'itertools.chain'>
for i in result:
    print(i)

#set
from itertools import chain
def chain_fun(l1,l2,l3):
    return chain(l1,l2,l3)
result=chain_fun({1,2,3,4}, {'a','b','c','d'}, {1,2,3,4,1,2,3,4,4})
print(type(result))   #<class 'itertools.chain'>
for i in result:
    print(i)

#write python program to generate running  produc of element in an iterable
from itertools import accumulate
import operator
def running_product(lst):
    return accumulate(lst,operator.mul)
lst=[1,2,3,4,5,4,5]
result=running_product(lst)
for i in result:
    print(i)
    
#if no function then it by default take addition for iteration
from itertools import accumulate
import operator
def running_product(lst):
    return accumulate(lst)
lst=[1,2,3,4,5,4,5]
result=running_product(lst)
print(type(lst))
for i in result:
    print(i)
    
#tuple
from itertools import accumulate
import operator
def running_product(lst):
    return accumulate(lst)
lst=(1,2,3,4,5,4,5)
result=running_product(lst)
print(type(lst))
for i in result:
    print(i)

#set
from itertools import accumulate
import operator
def running_product(lst):
    return accumulate(lst)
lst={1,2,3,4,5,4,5}
result=running_product(lst)
print(type(lst))
for i in result:
    print(i)

#write python program to construct infinite iterator that 
#returns evenly spaced values strating with a specified number and step
import itertools as it
start=10
step=1
my_counter=it.count(start,step)
for i in my_counter:
    print(i)

#write python program to generate the cycle of element from an iterable
import itertools  as it
def cycle_num(itr):
    return it.cycle(itr)
ls1=['A','B','C','D']
result=cycle_num(ls1)
for i in result:
    print(i)

#write python program to generate the cycle of string from an iterable
import itertools  as it
def cycle_num(itr):
    return it.cycle(itr)
ls1="Sanjivani College of Engg"
result=cycle_num(ls1)
for i in result:
    print(i)
#write a program to make an iterator that drops
#element from the iterables as soon as element ia a positive number
import itertools as it
def drop_while(nums):
    return it.dropwhile(lambda x:x<0, nums)
nums=[-1,-1,-1,1,2,3,4,-1,2,3,3]
result=drop_while(nums)
print("Drop element from the list when positive number occured\n",list(result))

    
    
    
    
    
    
    