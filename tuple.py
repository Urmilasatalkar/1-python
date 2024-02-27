# -*- coding: utf-8 -*-
"""
Created on Fri Jul 28 10:32:14 2023

@author: urmii
"""

###################################
#tuple
tuple=(1,6,3,4)
print(f'tuple[0]:\t{tuple[0]}')
print('tuple[1]:\t',tuple[1])
print('tuple[2]:\t',tuple[2])
print('tuple[3]:\t',tuple[3])

tup1=('jonh',12,12.5,True)
print(tup1)

#iterating over tuple
tup2=('mango','orange','kiwi','banana',12,12.45,'mango')
for i in tup2:
    print(i)
print(type(tup2))
len(tup2)  #6
tup2.count('mango')
tup2.count('mango')  #2
print(tup2.index('mango'))  #0
#checking element is present or not in tuple

if 'mango' in tup2:
    print("Yes,mango is present")
else:
    print("No")
    
if 'chikoo' in tup2:
    print("Yes,mango is present")
else:
    print("No")

tup1=(1,2,3,4)
tup2=('John','Mars','alex','adam','phoebe')
tup3=(23,tup1,24,tup2,7,7)
print(tup3)
