# -*- coding: utf-8 -*-
"""
Created on Fri Jul 28 09:43:32 2023

@author: urmii
"""
#read content from file
with open ('pi_digits.txt') as file_object:
    #the open() need a function
    contents=file_object.read()
print(contents)
    
#read content from file
#remove white space which is getting after output
#rstrip()
with open ('pi_digits.txt') as file_object:
    #the open() need a function
    contents=file_object.read()
print(contents.rstrip())

file_path='c:/1-python/pi_digits.txt'
with open (file_path) as file_object:
    #the open() need a function
    contents=file_object.read()
print(contents.rstrip())

#reading line by line
file_path='pi_digits.txt'
with open (file_path) as file_object:
    for line in file_object:
        print(line)
        
#reading line by line
file_path='pi_digits.txt'
with open (file_path) as file_object:
    for line in file_object:
        print(line.rstrip())
        
#working with a files content
#after you have read a file into memory
#you can do any opertion that you want
file_path='pi_digits.txt'
with open (file_path) as file_object:
    lines=file_object.readlines()
    pi_string=''
    for line in lines:
        pi_string=pi_string+line.rstrip()
        print(pi_string)
        print(len(pi_string))
        
#writing to a file   
file_name='programming.txt'
with open(file_name,'w') as file_object:
    file_object.write("I love programming")
     
#writing a multiple lines
#the write() function dosent give permission to add line on new line
file_name='programming.txt'
with open(file_name,'w') as file_object:
    file_object.write("I love programming")
    file_object.write("Hello,Sanjivani")

#writing a multiple lines
#add line on new lines()
file_name='programming.txt'
with open(file_name,'w') as file_object:
    file_object.write("I love programming\n")
    file_object.write("Hello, Sanjivani")

#appending a file
#append:add new content in file but old content will not vanish
file_name='programming.txt'
with open(file_name,'a') as file_object:
    file_object.write("I love Python\n")
    file_object.write("Hello World")






