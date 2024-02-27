# -*- coding: utf-8 -*-
"""
Created on Fri Jul 28 15:11:22 2023

@author: urmii
"""
#the error signifies a situation that mostly happend duw to absense of resources
#the exception are the issue that can appear at runtime and compile error
#it majorly arises in the code or program 
#autorized by developers

#Exception handling
#exception can handle with try-except block
#handling the ZeroDivisionError Exception
a=5
b=6
c=a+b
#without handling exception
print(5/0)

#using try-except block

#handling Exception
'''try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide 5 by zero")'''
print(c)
    
a=5
b=6
c=a+b
#using try-except block

#handling Exception
try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide 5 by zero")
    print(c)
    
#handling he filenotfounderror Exception
filename='alice.txt' 
try:
    with open(filename,encoding='utf-8') as f:
        content=f.read()
except FileNotFoundError:
    print(f"Sorry {filename} file  not found in your machine ")

    
    
    
    
    
    
    
    
    
    
