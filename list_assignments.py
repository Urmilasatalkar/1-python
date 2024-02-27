# -*- coding: utf-8 -*-
"""
Created on Thu Jul 27 14:32:36 2023

@author: urmii
"""
#Assignment

#take 5 nos in a list find out minimum of list
#maximum of list
#take 5 strings in the list make it reverse list
#take 10 nos in list write script to search for value
#take 10 nos in list insert some duplicate nos in list write scipt to find duplicates
# take vowels in list and non vowels letters find out total no vowels in list
l1=[3,5,1,6,8]
l2=min(l1)
print(l2)
print(max(l1))

#######################################################
#smaller number
small=l1[0]
for i in l1:
    if i<small:
        small=i
print("Smallest digit:",small)

############################################################
#larger number
large=l1[0]
for i in l1:
    if i>large:
        large=i
print("Largest digit:",large)

######################################################
#reverse list
l2=['apple','chikoo','plum','peter','orange']
l3=l2[::-1]
print("Reverse list:",l3)

 ##################################################### 
#search given number in list      
l4=[5,6,2,3,4,5,1,3,5,10]
def searchelement(n):
        if n in l4:
            print("Element present in list at index:",l4.index(n))
        else:
            print("Element not present in list")
n=int(input("Enter the number to search:"))
searchelement(n)

###################################################
#duplicate elements
l4=[5,6,2,3,4,5,1,3,5,10,10]
l6=[]
l7=[]
def duplielement():
    for i in l4:
        if i not in l6:
            l6.append(i)
        elif i not in l7:
            l7.append(i)
    print(l6)  
    #print(l7)
duplielement()
   
l4=[5,6,2,3,4,5,1,3,5,10,10]
l6=[]      
for i in l4:
        if l4.count(i)>=2:
            if l6.count(i)==0:
                l6.append(i)
print(l6)


#########################################################                
#vowels counting
l1=['a','e','f','d','g','o','o','u','i','I','K','O','A']
l2=[]
def vowels():
    count=0
    for i in l1:
        if i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or i=='O' or i=='E' or i=='U' or i=='I':
            l2.append(i)
            l2.count(i)
    print("Vowels:",l2)
    for i in l2:
        count=count+1
    print("Total vowels present in list:",count)
vowels()

#python program to add all the item in list
l1=[3,4,5,6,7]
def sumlist(l1):
    sum=0
    for i in l1:
        sum=sum+i
    print("Sum of elements is:",sum)
sumlist(l1)  

#python program to multiply all the item in list
l2=[3,4,5,6,7]
def mullist(l2):
    mul=1
    for i in l2:
        mul=mul*i
    print("Sum of elements is:",mul)
mullist(l2)  

#write a program to find largest number from list
l3=[3,4,6,7,8]
large=l3[0]
for i in l3:
   if i>large:
     large=i
print(large)

#smallest number from list
l3=[3,4,6,7,8]
small=l3[0]
for i in l3:
   if i<small:
     small=i
print("Smallest number:",small)

#write a program to count the string which length of string is 2 and first and last should same
l1=['abc','xyz','aba','1212']  
def countstring(l1) :
    ctr=0
    for i in l1:
        if len(i)>2 and i[0]==i[-1]:
            ctr+=1
    return ctr
countstring(l1)

#write a python program to get a list sorted in increasing order by the 
#last element in each tuple of tuple from  given list of non-empty tuples
sample_list=[(2,5),(1,2),(4,4),(2,3),(2,1)]  
#output=[(2,1),(1,2),(2,3),(4,4),(2,5)]
def last(n):
    return n[-1]   
def sorted_function(sample_list):
    result=sorted(sample_list,key=last)
    return result
sorted_function(sample_list)

#write a pragram to remove duplicates from list
l3=[3,4,5,6,7,1,2,3,8,9,3,4,4,4,]
dupli=[]
non_dupli=[]
def duplicates(l3):
    for i in l3:
        if i not in dupli:
            dupli.append(i)
        elif i not in non_dupli:
            non_dupli.append(i) 
    a=set(dupli)
    b=set(non_dupli)
    print(a-b)
duplicates(l3)
                       
##copy onr list into another list
l3=[3,4,5,6,7,1,2,3,8,9,3,4,4,4,]
l4=l3
print(l3)
print(l4)

#write a python program to find a list of words that are longer than n from a given list of words
word=['sanjivani','Urmila','set','list']
l=[]
def longerstring(n,word):
    for i in word:
        if len(i)>n:
            l.append(i)
    return l
longerstring(3, word)

#write a python program to find a list of words that are longer than n from a given list of words
def long_word(n,str):
    l=[]
    txt=str.split(" ")
    for i in txt:
        if len(i)>n:
            l.append(i)
    return l
print(long_word(3,"The quick fox jump over the lazy dog"))

#write a python program take two list and find common number from list
l1=[1,2,3,45,3,4]
l2=[2,3,4,5,678,6]
def commonlist(l1,l2):
    for i in l1:
        for j in l2:
            if i==j:
                return True
    return False
commonlist(l1, l2)
    
l1=[1,2,3,45,3,4]
l2=[2,3,4,5,678,6]
def commonlist(l1,l2):
    for i in l1:
         if i in l2:
                return True
    return False
commonlist(l1, l2)

#write python program to diff betwen two list
l1=[1,2,3,45,3,4]
l2=[2,3,4,5,678,6]
a=set(l1)
b=set(l2)
c=a-b
d=b-a
print(c)
print(d)
print(c | d)

#write a python to convert a list of charchter into a string
s={'a','b','c','d','g','r'}
str1=''.join(s)
print(str1)

#write a program to find out index of specific element
#important
l1=[1,2,3,45,3,4]
print(l1.index(3))      #example #recommendation list

#append one list into another list
l1=[1,2,3,45,3,4]
l2=[2,3,4,5,678,6]
l3=l1+l2
print(l3)

x='Hello, worlds'
print(x.split(','))
print(x.find('Hello'))

