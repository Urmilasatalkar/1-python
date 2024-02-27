# -*- coding: utf-8 -*-
"""
Created on Fri Jul 28 10:33:49 2023

@author: urmii
"""


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

