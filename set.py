# -*- coding: utf-8 -*-
"""
Created on Fri Jul 28 10:33:15 2023

@author: urmii
"""

#################################################
#set
#it will not count  duplicate elements
s1={'mango','chikoo','orange',2,4,5,5}
print(s1)
print(len(s1))
s1.remove('mango')
s1.discard('chikoo')
print(s1)
s1.add('Kiwi')  #add new elements
print(s1)
s1.update([1,3,4])
print(s1)
print(len(s1))
s3={1,2,35,32,2}
print(min(s3))
print(max(s3))

#set operations
s1={1,2,3,4}
s2={4,5,6,2}
print("Union:",s1 | s2)
print("Intersection:",s1 & s2)      
print("Difference:",s1-s2)
