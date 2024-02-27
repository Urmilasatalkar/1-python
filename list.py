# -*- coding: utf-8 -*-
"""
Created on Fri Jul 28 10:31:12 2023

@author: urmii
"""
#List
lst1=[1,2,3,4]
lst2=['urmila','john',12.0,'fruit']
print(lst1)
print(lst2)
lst3=[lst1,'mango','chikoo',lst2,1244]
print(lst3)
lst4=lst1+lst2 #concatenate
print(lst4)
print(lst1[0])
print(lst1[-1])

lst4=[1,2,3,4,'alex','plum','adam']
print(lst4)#4
print(lst4[-3])
print(lst4[:3])
print(lst4[1:])
print(lst4[-1])
print(lst4[1:3])
print(lst4[-1:-3:-1])
print(lst4[-3:-1])
print(lst4[::-1])
lst4.append('peter')
print(lst4)
lst4.extend(['vaish','Urmila','Rucha',2,3])#add whole list into present list
print(lst4)
lst4.insert(0,'Sanjivani')
print(lst4)
lst4.insert(-3,'Sanjivani')
print(lst4)

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
l1=[3,4,5,1,2,3,7,1,2,4]
small=l1[0]
for i in l1:
    if i<small:
        small=i
print(small)
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
def duplicate():
    for i in l4:
        if i not in l6:
            l6.append(i)
        elif i not in l7:
            l7.append(i)
    print(l6)
    print(l7)
duplicate()
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
    print("Vowels:",l2)
    for i in l2:
        count=count+1
    print("Total vowels present in list:",count)
vowels()
      
####################################
#remove elements
l1=[1,2,3,4,5,'sanjivani','peter','alex']
l1.remove('sanjivani')
print(l1)      
##########################################
#pop() it used to remove element from list but it differ from remove
#it required a index 
l1=[1,2,3,4,5,'sanjivani','peter','alex']
l1.pop(1)
print(l1) 






