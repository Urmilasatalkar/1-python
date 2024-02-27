# -*- coding: utf-8 -*-
"""
Created on Wed Jul 26 15:36:00 2023

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
    print(l7)    
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


#################################################
#set
#it will not duplicate elements
s1={'mango','chikoo','orange',2,4,5,5}
print(s1)
s1.remove('mango')
s1.discard('chikoo')
print(s1)
s1.add('Kiwi')
print(s1)
s1.update([1,3,4])
print(s1)
print(len(s1))
s3={1,2,35,32,2}
print(min(s3))
print(max(s3))

#set operations
s1={1,2,3,4}
s2={4,5,6,2}
print("Union:",s1 | s2)
print("Intersection:",s1 & s2)
print("Difference:",s1-s2)

############################################
#Dictionary
d1={'vaishnavi':1,'Rucha':14,'Urmila':26}
print(d1)
d2={'Rahul':1,'Virat':18,'Dhoni':7}
#accessing elements from dict
d3=d1['Urmila']
print(d3)
d3=d2['Dhoni']
print(d3)
#add new items in dict
d1['Harshalini']=29
print(d1)
#remove item from dict
d2.pop('Rahul')
print(d2)

print(d1.items())
print(d1.keys())
print(d1.values())
print('Urmila' in d1)
print('Urmila' not in d1)
print(len(d1))
#iterating dict
for i in d1:
    print(i,":",d1[i],end='  ') #vaishnavi:1 Urmila:26 Rucha:14

for i in d1:
    print(i,":",end='  ')  #it prints only keys
    print(d1[i])           #only values

for i in d1:
    print(d1[i], end='  ') #it print only values

season={'Summer':('feb','mar','april','may')
        , 'Rainy':('june','july','aug','sep'),
        'Winter':('oct','nov','dec')}
print(season['Rainy'])
print(season['Rainy'][2])
print(season.get('Summer'))

d1={'vaishnavi':1,'Rucha':14,'Urmila':26,'Urmila':13,'Shivani':12}
print(d1)

#python program to add all the item in list
l1=[3,4,5,6,7]
def sumlist(l1):
    sum=0
    for i in l1:
        sum=sum+i
    print("Sum of elements is:",sum)
sumlist(l1)  

