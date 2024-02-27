# -*- coding: utf-8 -*-
"""
Created on Fri Jul 28 10:36:31 2023

@author: urmii
"""
#by using lambda function
add=lambda a,b,c:a+b+c
add(4,5,6)

def multi(a,b,c):
    sum=a*b*c
    return sum
print(multi(4,5,6))
multi=lambda a,b,c:a*b*c
multi(4,5,6)

#when we dont know arguments 
val=lambda* args:sum(args)
val(2,3,4,5,6)
val(1,2,3,5,6,7,6,7,8)

def person(name,no,**data):
    print(name)
    print(data)
    print(no)
person('navin',123,age=18,place='Mumbai',phone=12121212)   
    
def person(name,**datait):
    print('Name:',name)
    for i,j in datait.items():
        print(i,':',j)     
person(name='navin',age=18,place='Mumbai',phone=12121212)   
    
#lambda function using keyword argument
val=lambda **data:sum(data.values()) 
val(a=1,b=2,c=3,d=4,e=5,f=6,g=6)

# lambda function using if else loop  
#max=lambda a,b:x if a>b #error should have else with if
#print(max(1,2))

max=lambda a,b:a if a>b else b
print(max(1,2))
    
max=lambda a,b:a if a>b else b
print(max(10,2))
    

