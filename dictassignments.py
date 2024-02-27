# -*- coding: utf-8 -*-
"""
Created on Fri Jul 28 16:42:56 2023

@author: urmii
"""
#write aprogram to add key to dictionary
d1={2:30,4:40,5:50,6:60,7:70}
d1.update({2:100})
d1[4]=400
print(d1)

#####################
#add key and value both into dictionary
d2={0:10,10:100}
print(d2)
d2[2]=30   #2:30
print(d2)

#################################
#write a python program to concatenate a dict to create a new one
#d1={1:10,2:20}
#d2={3:30,4:40}
#output={1:10,2:20,3:30,4:40}
d1={1:10,2:20}
d2={3:30,4:40}
d2=len(d1)
print(d2)
d3={}
for d in (d1,d2):
    d3.update(d)
print(d3)

###############################
#write a program to check weather key is present or not
d1={1:10,2:20,3:30,4:40,5:50,6:60,7:70}
def dicti(n):
    for i in d1:
        if n == d1[i]:
            print("Yes, given key is present")
            break
        else:
            print("Not present")
n=int(input("Enter a key :"))
dicti(n)

###########################################
#print key and value using looping
d1={1:10,2:20,3:30,4:40,5:50,6:60,7:70}
for i,j in d1.items():
    print(i,":",j,end="")
for i in d1:
    print(i,':',d1[i],end='')

##########################################
#== for checking the both dict are same or not
dict1 = {"key1":1, "key2":2}
dict2 = {"key2":2, "key1":1}
print(dict1 == dict2)

sampleDict = dict([
    ('first', 1),          #{'first': 1, 'second': 2, 'third': 3}
    ('second', 2),
    ('third', 3)
])
print(sampleDict)

#13. Select the correct way to print Emma’s age.
student = {1: {'name': 'Emma', 'age': '27', 'sex': 'Female'},
           2: {'name': 'Mike', 'age': '22', 'sex': 'Male'}}
stud=student[1]['age']
print(stud)

#Select the correct way to access the value of a history subject
sampleDict = {"class":{ "student":{ "name":"Mike","marks":{ "physics":70,"history":80}}}}
sampleDict["class"]["student"]["marks"]["history"]

#Even values it will print
d1={'Rucha':32,'Harshalini':29,'Urmila':26}
d2={k:v for (k,v) in d1.items() if v%2==0}
print(d2)

d1={'Rucha':32,'Harshalini':29,'Urmila':61}
d2={k:v for (k,v) in d1.items() if v%2!=0 if v>=26}
print(d2)

d1={'Rucha':32,'Harshalini':29,'Urmila':26}
d2={k:('old' if v<=30 else 'young') for (k,v) in d1.items()}
print(d2)




