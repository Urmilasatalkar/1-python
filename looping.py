# -*- coding: utf-8 -*-
"""
Created on Fri Jul 28 10:29:09 2023

@author: urmii
"""

num=int(input("enter the number:"))
if num>0:
    print(num)
    
    
    
num1=int(input("Enter the number:"))
if num1< 0:
    print("Its Negative")
else:
    print("It is positive")

print(3*3+3/3-3)
"""
Spyder Editor

This is a temporary script file.
"""
a=float(input('Enter a saving :'))
if a==0:
    print('Sorry no saving')
elif a<500:
    print('well Done')
elif a<1000:
    print('that is tidy sum')
elif a<1000:
    print('Welcome sir')
else:
    print('Thank you')
    
#while loop
count=1
while count<=10:
    print(count)
    count=count+1
#for loop
for i in range(2,10):
    print(i)
print('Done')

num=int(input('Enter a number:'))
for i in range(0,20):
    if i==num:
        break
    print(i)
print('Done')
#Anonymous variable
for _ in range(0,10):
    print('.',end=' ')
    print()
print('Done')
#.........
for _ in range(0,10):
    print('.',end=' ')
print('Done')

'''.

    .
    
    .
'''
for _ in range(0,10):
    print('.')
    print()
print('Done')

####################################
num=int(input('Enter Number:'))
for i in range(0,20):
    if i==num:
        break;
    print(i,' ',end='')
    print('Done')
    
# odd numbers
start, end=4,20
for i in range(start,end+1):
    if i%2!=0:
        print(i,' ',end='')
        
 #Even number   
start,end=2,20
for i in range(start,end+1):
    if i%2==0:
        print(i,' ',end='')
        
#print number by incrementing it by 2
#Even number
for i in range(2,15,2):
    if i%2==0:
        print(i,' ',end='')
   
#ODD number
for i in range(3,25,2):
    if i%2!=0:
        print(i,' ',end='')
        
#input from user
#EVEN
num1=int(input('Enter a num1:'))
num2=int(input('Enter a num2:'))
for i in range(num1,num2+1):
    if i%2==0:
        print(i,' ',end=' ')
#ODD
num1=int(input('Enter a num1:'))
num2=int(input('Enter a num2:'))
for i in range(num1,num2+1):
    if i%2!=0:
        print(i,' ',end=' ')
        
        