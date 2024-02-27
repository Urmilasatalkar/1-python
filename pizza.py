# -*- coding: utf-8 -*-
"""
Created on Wed Jul 26 10:21:51 2023

@author: urmii
"""
#argument+arbitary code
def arbi(size,*toppings):
    print(f"Size of pizza:{size}")
    for topping in toppings:
        print(f"{topping}")
arbi(12,'pepproni')
arbi(17,'mushrooms','cheese','peppers')

def listi(usernames):
    for name in usernames:
        msg=f"Hello,{name.title()}"
        print(msg)
usernames=['Rucha','Harsha','Urmila','Ram','Alex','Sanket']
listi(usernames)

def arbi1(*toppings):
    print(toppings)
arbi1('pepproni')
arbi1('mushrooms','cheese','peppers')
