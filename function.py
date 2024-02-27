# -*- coding: utf-8 -*-
"""
Created on Tue Jul 25 10:17:01 2023
@author: urmii
"""
##################################
#Prime number
def myfun(num):
    for i in range(2,num):
        if num%i==0:
            print("Not prime number")
            break
        else:
            print("Prime number")
num=int(input("Enter a number :"))
myfun(num)
#################################
#function without arguments
def greet_user():
    print("Hello I'm Urmila")
greet_user()
#########################################
##passing argument in function
def argument(user):
    print(f"Hello I'm {user}")
user=str(input("Enter String :"))
argument(user)
#######################################
#Positional argument
def argument(typeanimal,name):
    print(f"Type is: {typeanimal}")
    print(f"Name is: {name}")
argument("Dog","Moti")
argument("Cat","Mau")

#Default values
def argument(typeanimal,name='Moti'):
    print(f"Type is: {typeanimal}")
    print(f"Name is: {name}")
argument("Dog")
argument("Cat")

#Avoiding arguments error
def argument(typeanimal,name):
    print(f"Type is: {typeanimal}")
    print(f"Name is: {name}")
argument()
####################################
bill=0
def calc(height,age):
    if height>=120:
        print("Welcome to rolllar Coaster")
        print("You are Eligible for playing Roller Coaster")
        if age<=18 and age>=12 and height==120:
            print("Your ticket of 15RS.")
            bill=15
        elif age>18:
            print("Your ticket of 50RS.")
            bill=50
        elif age<=12 and height==120:
            print("Your ticket of 10RS.")
            bill=10
        elif age<18:
            print("Your ticket of 20RS.") 
            bill=20
        photo=input("Do you want photo 'Y' or 'N'")
        if photo=='Y' or'y':
            bill=bill+20
            print("Your final bill is: ",bill)
        else:
            print("You can proceed further")
    else:
        print("You are not Eligible for playing Roller Coaster")
height=int(input("Enter your Height:"))
age=int(input("Enter your age:"))
calc(height,age)
######################################
def yearcalc(currage,days):
    countyears=80-currage
    totaldays=countyears*365
    r_maindays=totaldays-days
    print()
    print("Remaining days:",r_maindays)
    month=r_maindays//30
    print("Total remaining months:",month)
    remain_days=r_maindays%30
    remain_weeks_days=remain_days%7
    if remain_days>=7:
        week=remain_days//7
        print("Remaining weeks are:",week,"and Remaining days are:",remain_weeks_days)
    else:
        print("Remaining days are:",remain_weeks_days)
currage=int(input("Enter your current age:"))
days=int(input("Enter your days:"))
yearcalc(currage,days)
#######################################     
users=['manager','employee','staff','worker','admin']
for user in users:
    if user=='manager':
        print("Hello manager")
    elif user=='employee':
        print("Hello Employee")
    elif user=='admin':
        print("Hello admin,would you like to see a status report??")
    elif user=='worker':
        print("Helllo worker")
    else:
        print("Hello")
 ###################################3
# password picker   
import string
adjective=['go','slowly','good','bad','fluffy','smily','red','green','balck','white']
noun=['ram','sita','i','you','vaishnavi','rucha','urmila','shivani','harsha','panda','goat','dragon']
import random
adjectives=random.choice(adjective)
nouns=random.choice(noun)
number=random.randrange(0,100)
special_char=random.choice(string.punctuation)
password=adjectives+nouns+str(number)+special_char
print("Random password for you:",password)

##############################################
#generate random password
import string
adjective=['go','slowly','good','bad','fluffy','smily','red','green','balck','white']
noun=['ram','sita','i','you','vaishnavi','rucha','urmila','shivani','harsha','panda','goat','dragon']
import random
print("Welcomw to password picker")
while True:
    adjectives=random.choice(adjective)
    nouns=random.choice(noun)
    number=random.randrange(0,100)
    special_char=random.choice(string.punctuation)
    password=adjectives+nouns+str(number)+special_char
    print("Random password for you:",password)
    ans=input("You want to generate password?? Y or N")
    if ans=='N'or ans== 'n':
        break
########################################################
#write password 
'''1.has one upper
has one lower
has minimum 8 character
has minimum one number?'''
def password(passw):
    has_lower=False
    has_upper=False
    has_num=False
    for ch in passw:
        if ch>='A' and ch<='Z':
            has_upper=True
        elif ch>='a' and ch<='z':
            has_lower=True
        elif ch>='0'and ch<='9':
            has_num=True
    if len(passw)>=8 and has_upper and has_lower and has_num:
        return True
    else:
        return False
passw=input("Enter a password:")
pa=password(passw)
if pa==True:
    print("your Password is strong")
else:
    print("Your password is weak")
#######################################################   
#pizza delivery
bill=0
def pizza(size):
    if size=='s':
        bill=15
    elif size=='m':
        bill=20
    elif size=="l":
        bill=25
    if add_pep=='Y'or add_pep=='y':
        if size=='s':
            bill=bill+2
        elif size=='m' or size=='l':
            bill=bill+3
    if add_cheese=='Y' or add_cheese=='y':
        if size=='s' or size=='m' or size=='l':
            bill=bill+1
    return bill
size=str(input("Enter size of pizza:"))
add_pep=input("Do you want extra pepprani:[Y|N]:")
add_cheese=input("Do you want extra chesse [Y|N]:")
print("Your final bill is:",pizza(size))
###############################################
#return a dict using function
def dict(first,last):
    person={'first':first,'last':last}
    return person
p=dict('Ram','Alexa')
print(p)

############################
#return a list using function 
#passing a list
def listi(usernames):
    for name in usernames:
        msg=f"Hello,{name.title()}"
        print(msg)
usernames=['Rucha','Harsha','Urmila','Ram','Alex','Sanket']
listi(usernames)
################################################
#Arbitaray numbers of argument
def arbi(*toppings):
    print(toppings)
arbi('pepproni')
arbi('mushrooms','cheese','peppers')
####################################################
#print multiple times 
def arbi(*toppings):
    for i in toppings:
        print(f"-{i}")
arbi('pepproni')
arbi('mushrooms','cheese','peppers')
########################################################
#print multiple times 
'''def arbi(*toppings):
    while i!=None:
        print(f"-{i}")
        i=next(toppings)
arbi('pepproni')
arbi('mushrooms','cheese','peppers')
'''
###################################################
#argument+arbitary code

def arbi(size,*toppings):
    for topping in toppings:
        print(f"-{topping},-{size}")
arbi(12,'pepproni')
arbi(17,'mushrooms','cheese','peppers')

#import file
import pizza
arbi(17,'mushrooms','cheese','peppers')

#import specific function
from pizza import arbi1
arbi1('mushrooms','cheese','peppers')

#using as to give a function an alias
from pizza import arbi1 as a
a('mushrooms','cheese','peppers')

#using as to give a module an alias
import pizza as a
a.arbi1('mushrooms','cheese','peppers')

#import all function in module
from pizza import*
arbi1('mushrooms','cheese','peppers')

#scope of valiable
#you cannot a ref a variable
x=0
x=x+1
x=6
print(x)  #6

x=6  #7
x=x+1
print(x)
#######################
#Normal function
def add(a,b,c):
    sum=a+b+c
    return sum
print(add(4,5,6))


