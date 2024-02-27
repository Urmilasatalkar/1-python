# -*- coding: utf-8 -*-
"""
Created on Tue Aug  1 10:34:39 2023

@author: urmii
"""
#####################################
#Combinations
from itertools import combinations
player=['john','johny','janardan']
for p in combinations(player,2):
    print(p)

#Permutaions
from itertools import permutations
player=['john','johny','janardan']
for p in permutations(player,2):
    print(p)
    
#product()
from itertools import product
l1=['mango','fruit','college']
l2=['fruit','mango','orange']
for i in product(l1,l2):
    print(i)
########################################
#it is a itertool for filtering the list oh the basis of condition
age=[2,3,4,5,61,23,12,34,23]
adults=filter(lambda age:age>=18,age)
print([age for age in adults])











