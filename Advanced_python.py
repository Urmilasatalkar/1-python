 # -*- coding: utf-8 -*-
"""
Created on Mon Jul 31 09:25:36 2023

@author: urmii
"""
#without list comprehension
lst=[]
for i in range(0,20):
    lst.append(i)
print(lst)
##################################################################
#List compression
lst=[i for i in range(0,20)]
print(lst)

l1=['Dada','kaka','mama']
lst=[i.capitalize() for i in l1]
print(lst)

#even number
#if else condition in right side
#buisness logic in left side
lst=[i for i in range(0,20) if i%2==0]   #[0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
print(lst)

#by using function
def even(num):
    return num%2==0
lst=[num for num in range(0,20) if even(num)]   #[0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
print(lst)
    
#finding vowels

#nested for loop using list comprehension
#output=['00', '01', '02', '10', '11', '12', '20', '21', '22']
lst=[f"{x}{y}" for x in range(3) for y in range(3)]   #nested looping    
print(lst)
##########################################################
#set comprehension
s1={x for x in range(0,10)}      #{0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
print(s1)

##########################################################
#Dictionary comprehension
d1={x:x*x for x in range(5)}  #{0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
print(d1)

d1={x:"EVEN" for x in range(5) if x%2==0}  #{0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
print(d1)

d1={x:x%2==0 for x in range(5)} 
print(d1)

def even(x):
    return x%2==0
d1={x:x for x in range(5) if even(x)} 
print(d1)
d1=[x for x in range(0,20) if even(x)]
print(d1)
################################################
#Genrertor
#it return multiple values
#it usese keyword yeild
#instead of using return keyword it uses yeild keyword
#when we use tuple comprehension,one object will be createdand we can access values of that 
# object using for loops
# generator is for tuple
gen=(x for x in range(0,20))
print(gen)                 #it will not print values directly it create object first
for x in gen:
    print(x)
  
#next() method
gen=(x for x in range(3))
next(gen)  

#function which return multiple values
def range_num(end):
    for num in range(0,end,3):
        yield(num)
for num in range_num(10):
    print(num)

def range_num(end):
    for num in range(1,end,1):
        if num%2==0:
            yield(num)
for num in range_num(10):
    print(num)

gen=range_num(10)
next(gen)
next(gen)
next(gen)
#######################################################

#Enumreate
#without Enumerate
lst=['Milk','Bread','Egg']
for index in range(len(lst)):
    print(f"{index+1} {lst[index]}")
    print(f"{index+1} {lst[index]}")

#with Enumerate
lst=['Milk','Bread','Egg']
for index,item in enumerate(lst,start=1):
    print(f"{index} {item}")

    #find common number from two list 
l1=[1,2,3,4]
l2=[3,4,5,6]
common=[a for a in l1 if a in l2]
print(common)
common=[a for a in l1 if a not in l2]
print(common)
common=[a for a in l2 if a not in l1]
print(common)
############################################################   
#Assignment 
#only print that number which is divisible by 7
lst=[i for i in range(1,1000) if i%7==0]
print(lst)    
 
#only print that number which have 3 in them
lst=[i for i in range(1,1000) if '3' in str(i) ]
print(lst)    
  
#count the number of spaces in string
string="Sanjivani college of engineering kopargaon"
c=0
lst=[i for i in string if i==' ']
print(len(lst))

#print only consonant
string="Sanjivani college of engineering kopargaon"
lst=[i for i in string if i not in 'a,e,i,o,u ," "']
print(lst)

#print only vowels
string="Sanjivani college of engineering kopargaon"
lst=[i for i in string if i in 'a,e,i,o,u ," "']
print(lst)
  
    
#############################################################
#get only the numbers in a sentence 
sentence="i was born in 2002 currently I am live in 2023"
words=sentence.split(" ")
lst=[i for i in words if not i.isalpha()]
print(lst)

#Even and odd by using list comprehension
lst={i:"Even" for i in range(0,20) if i%2==0}
print(lst)

lst=['EVEN' if i%2==0 else 'ODD' for i in range(1,21)]
print(lst)
#same number in one tuple
l1=[1,2,3,4,1,2,3,4]
l2=[3,4,5,6,2,3,4,5]
lst=[(i,j) for i in l1 for j in l2 if i==j]
print(lst)

#same word in one tuple
str1='I am Urmila'
str2='I am Vaishanvi and my frnd name is Urmila'
w1=str1.split(" ")
w2=str2.split(" ")
lst1=[(i,j) for i in w1 for j in w2 if i==j ]
print(lst1)

#print string whose length >=4
s1="Sanjivani college Dream city ok "
w1=s1.split(" ")
lst=[ i for i in w1 if len(i)>=4]
print(lst)

#write a python program to print a spacified list
#after removing 0th,4th and 5th elements
color=['red','green','black','yellow','peach'] #op->['green', 'black', 'yellow']
lst=[x for (i,x) in enumerate(color) if i not in (0,4,5)]#i-index and x-value
print(lst)
l1=[x for i,x in enumerate(color) if i not in (0,4,5)]
print(l1)
clr=[i for i in color if i not in i[0]]
print(clr)
#write python program to generator function that is cubes of number from 1 to n
#accept n from user
def range_cube(num):#generator function
     for i in range(1,num+1):
         yield(i**3)
num=int(input("Enter number:"))
for num in range_cube(num):
    print(num)

cube=range_cube(num)
next(cube)
next(cube)
next(cube)

#write a python program to implement a gene that generates
#random number within given range
import random
def random_num(start,end):
    while True:
        yield random.randint(start,end)
start=int(input("Enter Start :"))
end=int(input("Enter End:"))
for i in range(start,end):
    print(i)
 
import random
def random_nu(start,end):
    while True:
        yield random.randint(start,end)
start=int(input("Enter Start :"))
end=int(input("Enter End:"))
ran_number=random_num(start, end)
for _ in range(10):
    randomn=ran_number
    print(next(randomn))
    
#write a program to generate 3*4*6 #D array whose elemet is * 3 rows 4 cols 6 cols
array=[[['*' for col in range(6)] for col in range(4)]for col in range(3)]
print(array)

#write a python program to print the numbrs of a specified
#list after remove even number from it
l1=[2,3,4,5,6,78,6]
lst=[i for i in l1 if i%2!=0]
print(lst)
  
################################################################### 
#1-aug-2023 
#zip function()
#important for interview
l1=['Dada','Mama','Kaka']
l2=[1200,1300,1400]
for name,info in zip(l1,l2):
    print(name,info)
    
l1=['Dada','Mama','Kaka']
l2=[1200,1300,1400,1500,1600]
for name,info in zip(l1,l2):
    print(name,info)
    
#zip longest() to overcome the previous drawback
from itertools import zip_longest 
l1=['Dada','Mama','Kaka']
l2=[1200,1300,1400,1500,1600]
for name,info in zip_longest(l1,l2):
    print(name,info) #NONE

#it will assign 0 instead of None      
#because in ML module it will not allowed none so we need to fill the some value instead of None
from itertools import zip_longest 
l1=['Dada','Mama','Kaka']
l2=[1200,1300,1400,1500,1600]
for name,info in zip_longest(l1,l2,fillvalue=0):
    print(name,info) 
##########################################################   
#use all() all the value are true  then it will produce output
#in feature engineering this topic will use
l1=[1,2,3,4,5,6,7,-10]
if all(l1):
    print("All values are true")
else:
    print("Useless")    
#if in list 0 element is present it will print useless
l1=[1,2,3,4,5,6,7,0]
if all(l1):
    print("All values are true")
else:
    print("Useless")    

########################################
#any() if any non zero value
l1=[4,5,0,0]
if any(l1):
    print("It has some non zero value")
else:
    print("Useless")       

#if all zero then it give useless
l1=[0,0,0,0]
if any(l1):
    print("It has some non zero value")
else:
    print("Useless")    
  
########################################
#count()
from itertools import count
counter=count()
print(next(counter))
print(next(counter))
print(next(counter))

#######################################
#now let ue start from 1
from itertools import count
counter=count(start=1)
print(next(counter))
print(next(counter))
print(next(counter))

#cycle()
#suppose you have repeated task to be done then you can use this method
import itertools
instruction=('eat','code','repeat')
for i in itertools.cycle(instruction):
    print(i)
    
#repeat()
from itertools import repeat
for msg in repeat("Keep going................!!!!" ,times=3):
    print(msg)
    
#Using lambda and sorted() function, sort the list 
#based on the remainder from dividing each element to 5
#(From greater to smaller).
lst1=[1000, 50, 66, 101, 333, 9999, 19, 300, 200, 250]
lst3=sorted(lst1)
print(lst3[-3])
lst2=sorted(lst1,key=lambda x:x%5,reverse=True)
print(lst2)