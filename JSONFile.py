# -*- coding: utf-8 -*-
"""
Created on Fri Jul 28 16:10:46 2023

@author: urmii
"""

import json
number=[2,3,4,5,6]
filename= 'number.json'
with open(filename,'w') as f:
    json.dump(number,f)  #dumb the data into file
    
#saving data with json is useful
#when ur working with user-generated data
import json
username=input("What is your name:")
filename='username.json'
with open(filename,'w') as f:
    json.dump(username,f)
print(f"we will remember you when you came back, {username}")

#now lets write anew program that greets
#a user whose name has already been stored 
import json
filename='username.json'
with open(filename,'w') as f:
    username=json.load(f)
    print(f"Welcome back, {username}")
    
#using try and exception
import json
filename='username.json'
try:
    with open(filename) as f:
        username=json.load(f)
except FileNotFoundError:
    username=input("What is your name:")
    with open(filename,'w') as f:
        json.dump(username,f)
    print(f"we will remember you when you came back, {username}")
else:
    print("welcome back , {username}")
    
    
    
    
    
    
    
    
    
    
    
    
    
    