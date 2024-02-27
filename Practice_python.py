# -*- coding: utf-8 -*-
"""
Created on Wed Aug 16 20:11:03 2023

@author: urmii
"""

l1=[1,2,3,4,5,6]
l3=l1[0]
l1[0]=l1[-1]
l1[-1]=l3
print(l1)

#swap first and last element
l1=[1,2,3,4,5,6]
size=len(l1)
l3=l1[0]
l1[0]=l1[size-1]
l1[size-1]=l3
print(l1)

l1=[1,2,3,4,5,6,1,0]
min(l1)
max(l1)
def mini(l1):
    fist=l1[0]
    for i in l1:
        if i<fist:
            fist=i
    print(i)
mini(l1)

l1=[1,2,3,4,5,6]
def mini(l1):
    fist=l1[0]
    for i in l1:
        if i>fist:
            fist=i
    print(i)
mini(l1)

l1=[2,3,4,1,2,3,4,2]
l1[::-1]
l1.clear()
print(l1)
def searchele(n):
        if n in l1:
            print('true')
        else:
           print('false')
n=4
searchele(n)


l2=[2,3,4,5,62,3,3]
l3=[]
l4=[]
for i in l2:
    if i not in l3:
        l3.append(i)
    elif i not in l4:
        l4.append(i)
print(l3)
print(l4)

l1=[2,3,4,1,2,3,4,2]
def searchelement(n):
    count=0
    for i in l1:
        if n==i:
            count=count+1
    print(count)
n=2
searchelement(n)

l1=[1,2,3,3,4,5,22,3,2,2,3,3,2,3,3,2]
def avg(l1):
    l=len(l1)
    sumo=0
    for i in l1:
        sumo=sumo+i
    print(sumo)
    avg=sumo/l
    print(avg)
avg(l1)

l1=[1,2,3,3,4,5,22,3,2,2,3,3,2,3,3,2]
l2=[]
for i in l1:
    if i%2==0:
        l2.append(i)
print(l2)

l1=[1,2,3,3,4,5,22,3,2,2,3,3,2,3,3,2]
l2=[i**2 for i in l1 if i%2==0]
print(l2)
l2=[]
count=0
for i in l1:
    if i%2!=0:
        l2.append(i)
        count=count+1
print(count)  
print(l2)       

l5=[(),1,2,3,4,3,1,3,4,(),23,()]
for i in l5:
    if (len(i)==0):
        l5.remove(i)
print(l5)

start=1
end=20
l1=[]
for i in range(start,end+1):
    if i>=0:
        l1.append(i)
print(l1)

l1=[1,2,3,2,1,1,2,3,4,3,2,-1,-2,-3,0,-1,-2,-3,-4,-3]
l2=[]
count=0
for i in l1:
    if i<0:
        l2.append(i)
        count=count+1
print(l2)
print(count)      

d1={'A':12,'B':1,'C':123,'D':102}
for i in d1:
    print(i,':',d1[i],end=' ')

d4=d1['A']
print(d4)
d1.values()
d1['Harsha']=12
print(d1)
d1['A']=101
print(d1)

d1={'Summer':('jan','feb','mar'),
    'Rainy':('april','may','june'),
    'winter':('july','Aug','sep')
    }
print(d1)
d1['Summer']
d1['Summer'][2]
for i in d1:
    print(i,':',d1[i],end='')

list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lily"]
l1=[]
for i , j in zip(list1,list2):
    print(i+j,end=' ')
    l1.append(i+j)
print(l1)
       
numbers = [1, 2, 3, 4, 5, 6, 7]
l2=[i**2 for i in numbers]
print(l2)

list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]
l3=[]
for i in list1:
    for j in list2:
        l3.append(i+j)
print(l3)
    
list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]
for i,j in zip(list1,list2[::-1]):
    print(i,j)

list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]
list1.remove("")
print(list1)

list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
list1[2][2].append(7000)
print(list1)

list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
# sub list to add
sub_list = ["h", "i", "j"]
list1[2][1][2].extend(sub_list)
print(list1)

list1 = [5, 10, 15, 20, 25, 50, 20]
index=list1.index(20)
list1[index]=200
print(list1)

list1 = [5, 20, 15, 20, 25, 50, 20]
l1=[i for i in list1 if i!=20]
print(l1)

for i in list1:
    if i==20:
        list1.remove(i)
print(list1)

keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
# empty dictionary
res_dict = dict()
for i in range(len(keys)):
    res_dict.update({keys[i]: values[i]})
print(res_dict)

    
dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
dict1.update(dict2)
print(dict1)
#second way
dict3=dict1.copy()
dict3.update(dict2)
print(dict3)

sampleDict = {
    "class": { "student": {"name": "Mike","marks": {"physics": 70,"history": 80}}}}

sampleDict['class']['student']['marks']['history']

employees = ['Kelly', 'Emma']
defaults = {"designation": 'Developer', "salary": 8000}
res=dict.fromkeys(employees,defaults)
print(res)


sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"}

# Keys to extract
keys = ["name", "salary"]
d1=dict()
for j in keys:
        d1.update({j:sample_dict[j]})
print(d1)

sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"}

# Keys to extract
keys = ["name", "salary"]
d1=dict()
for j in keys:
        sample_dict.pop(j)
print(sample_dict)













