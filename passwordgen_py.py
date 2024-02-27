# -*- coding: utf-8 -*-
"""
Created on Tue Aug 22 20:51:10 2023

@author: urmii
"""

#chaining generators
password=['mango-fruit','you-you','not-good']
def length(itr):
    for ele in itr:
        yield len(ele)
def hide(itr):
    for ele in itr:
        yield  ele*'*'
for i in hide(length(password)):
    print(i)
    
##########################################################    
import string
adjective=['go','slowly','good','bad','fluffy','smily','red','green','balck','white']
noun=['ram','sita','i','you','vaishnavi','rucha','urmila','shivani','harsha','panda','goat','dragon']
import random
adjectives=random.choice(adjective)
nouns=random.choice(noun)
number=random.randrange(0,100)
special_char=random.choice(string.punctuation)
passwords=adjectives+nouns+str(number)+special_char
print("Random password for you:",passwords)
def length(itr):
    for ele in itr:
        yield len(ele)
def hide(itr):
    for ele in itr:
        yield  ele*'*'
for i in hide(length(passwords)):
    print(i,end="")