# -*- coding: utf-8 -*-
"""
Created on Wed Aug 16 15:51:11 2023

@author: urmii
"""

from PyPDF2 import PdfFileReader
#import required modules
from PyPDF2 import PdfReader

#creating a pdf reader object
reader=PdfReader('c:/1-python/python_tutorial.pdf')

#getting a specific page from pdf document
page=reader.pages[10]
print(page)

#extracting text from pdf
text=page.extract_text()
print(text)

import re
text='hi I have a problem with my order number 412889912'
pattern=r'number (\d+)'
match=re.findall(pattern,text)
print(match)

import re
text='hi I have a problem with my order number 412889912'
pattern=r'order[^\d]*\d*'
match=re.findall(pattern,text)
print(match)

#we only want number
import re
text='hi I have a problem with my order number 412889912'
pattern=r'order[^\d]*(\d*)'
match=re.findall(pattern,text)
print(match)

#we only want number
import re
text='hi I have a problem with my order number 412889912'
pattern=r'order * [^\d]*(\d*)'
match=re.findall(pattern,text)
print(match)

#we only want number using # instead of text
import re
text='hi I have a problem with my order # 412889912'
pattern=r'order * [^\d]*(\d*)'
match=re.findall(pattern,text)
print(match)

import re
text='hi: my order 122354556566 is having an issue I was charged 300$ '
pattern=r'order * [^\d]*(\d*)'
match=re.findall(pattern,text)
print(match)

def get_pattern_match(pattern,text):
    match=re.findall(pattern,text)
    if match:
        return match[0]
get_pattern_match('order * [^\d]*(\d*)', text)

#email iD match
chat1='Hello I am Alex_12@gmail.com'
pattern=r'[a-zA-z0-9_]*@{1}[a-z]*\.[a-zA-z0-9]*'
#/[a-zA-z0-9_]*@[a-z]*[.][a-zA-z0-9]* another way 
match=re.findall(pattern,chat1)
print(match)

#word tokenization
import re
text='hi I have a problem with my order # 412889912'
line = 'asdf fgdk; afed fjek, askd, foo'
re.split(r'(?:;,|;|\s)\s*',line)
##########################################
pattern = r'(?:,|;|\s)\s*'
re.split(pattern, text)
#################################

#matching text at start or end of string 
import nltk
filename = 'spam.txt'
filename.endswith('.txt')

##########################################

area_name = '6 th lane west andheri'
area_name.endswith('west andheri')

####################################
choices = ('http:','ftp:')
url = 'http://www.python.org'
url1 = 'https://www.python.org'
url.startswith(choices)
url1.startswith(choices)
######################################
#slicing of string
#if S is a string then expression of S [start:stop:update/step]

s = 'AEDSFFFFKGKJGNGNJJFKEKFLEK'
print(s[3:7])
#slicing with negative indices

print(s[-7:-10:-1])#in reverse order
print(s[-7:-1])#in serial order

print(s[::-1])#reverse string

#specify the steps in slicing

#alternate 
print(s[::2])

print(s[1:17:3])

s[:3]

#slice last 3 chars from string
len(s)
s[-3:]

#reverse a string

s[::-1]
#similar operations that can be done with slicing
filename = 'abc.txt'
filename[-4:] == '.txt'

############################################

url = 'http://www.python.org'

url[:5] == 'http:'
url1[:5] == 'http:'

url[:5] == 'http:' or url[:4] == 'ftp:' or url[:6]=='https:'

#################################

#fnmatch package
from fnmatch2 import fnmatch2, fnmatchcase2
names = ['Dat1.csv','Dat2.csv','config.ini']
[name for name in names if fnmatch2(name,'Dat*.csv')]

###############################
addresses = [
    '5142 N CLARK ST',
    '1060 W ADDISON ST',
    '2234 W GRANVILLE AVE',
    '2199 N CLARK ST',
    '2234 N VILLE AVE',
    '2313 N BROADWAY'
    ]

from fnmatch2 import fnmatch2, fnmatchcase2
[addr for addr in addresses if fnmatchcase2(addr,'*ST')]
#op --> ['5142 N CLARK ST', '1060 W ADDISON ST', '2199 N CLARK ST']

[addr for addr in addresses if fnmatchcase2(addr,'*AVE')]
#op --> ['2234 W GRANVILLE AVE', '2234 N VILLE AVE']
####################################

text = 'yeah, but no, but yeah, but no, but yeah'
#exact match
text == 'yeah'
#false
#match at start or end

text.startswith('yeah')
text.endswith('yeah')

###############################
#it returns the position of word to search in string
text.find('no')
#op --> 10

#################
text1 = '11/27/2012'
text2 = 'Nov 27, 2012'
import re
if re.match(r'\d+/\d+/\d+', text1):
    print("match found",text1)
else:
    print("Not found")
    
if re.match(r'\d+/\d+/\d+', text2):
    print("match found",text2)
else:
    print("Not found")
    
if re.match(r'(a-zA-Z)(\d+)(\d+)',text2):
    print("match found",text2)
    
###############################
datepat = re.compile(r'(\d+)/(\d+)/(\d+)')
if re.match(datepat,text2):
    print("yes")
else:
    print("No")

text = 'yeah, but no, but yeah, but no, but yeah'
text.replace('yeah','yep')

#############################
#if you have dates in format 11/27/2012 want to convert 2012-11-27
#substitution function
text = 'today is 11/27/2012. pycon starts with 3/13/2013'
import re
re.sub(r'(\d+)/(\d+)/(\d+)',r'\3-\1-\2',text)
#3rd grp - 1st grp - 2nd grp

#op->> today is 2012-11-27. pycon starts with 2013-3-13 
##################

#if you want to know how many substitutions are done
newtext,n = datepat.subn(r'\3-\1-\2', text)
print(newtext,"\n",n)

##########################
#matching or substituting word in text
text = 'UPPER PYTHON, lower python, Mixed Python'
re.findall('python',text,flags=re.IGNORECASE)

re.findall('PyThoN',text,flags=re.IGNORECASE)

re.sub('python','sNaKe',text,flags = re.IGNORECASE)
#op-->>'UPPER sNaKe, lower sNaKe, Mixed sNaKe'
############################

#matching or substituting text in same pattern as that of matched word in text
import re
def matchcase(word):
    def replace(m):
        text = m.group()
        if text.isupper():
            return word.upper()
        elif text.islower():
            return word.lower()
        elif text[0].isupper():
            return word.capitalize()
        else:
            return word
    return replace

text3 = re.sub('python',matchcase('snake'),text,flags = re.IGNORECASE)
text3

#'UPPER SNAKE, lower snake, Mixed Snake'

#################################
#
str_pat = re.compile(r'\"(.*)\"')
text1 = 'computer says "NO"'
str_pat.findall(text1)
#op--> ['NO']


##################################

#suppose we have text like,,
text2 = 'computer says "NO", phone says "yes"'
str_pat.findall(text2)
#op->>> ['NO", phone says "yes']
#it also gives phone says in output but expected is only yes and no

str_pat1 = re.compile(r'\"(.*?)\"')
str_pat1.findall(text2)
#['NO', 'yes']

###############################
#if you want to remove comment

str_pat2 = re.compile(r'/\*(.*)\*/') #pattern for comment
text1 = '/* this is comment*/'
str_pat2.findall(text1)

text2 = '''/* this is a 
        multiline comment*/
'''
comment_mult = re.compile(r'/\*((?:.|\n)*?)\*/')
comment_mult.findall(text2)

comment_mult = re.compile(r'/\*((?:.|\n)*?)\*/',re.DOTALL)
comment_mult.findall(text2)


comment = re.compile(r'/\*(.*?)\*/',re.DOTALL)
comment.findall(text2)

####################################
#normalizing unicode text to standard representation

#encoding

s1 = 'Spicy Jalape\u00f1o'
s2 = 'Spicy Jalapen\u0303o'
print(s1)
print(s2)
s1==s2
#false
#############################
import unicodedata2 
t1 = unicodedata2.normalize('NFC',s1)
t2 = unicodedata2.normalize('NFC',s2)
t1==t2

#Encoding
string1='apple'
string2='jeei125'
string3='12345'
string4='pre@12'
string1.encode(encoding='UTF-8',errors='strict')
string2.encode(encoding='UTF-8',errors='strict')
string3.encode(encoding='UTF-8',errors='strict')
string4.encode(encoding='UTF-8',errors='strict')

text= 'one 🐘 and three 🐋'
print(text)
print(len(text))

e=text.encode('utf8')
print(e)
print(len(e))

fname='data.txt'
with open(fname, mode='rb') as f:
    contents=f.read()
    print(type(contents))
    print(contents)
    print(contents.decode('utf8'))

#same way by using utf=18
text= 'one 🐘 and three 🐋'
print(text)
print(len(text))

e=text.encode('utf16')
print(e)
print(len(e))

#rb=open the file in binary format for reading
fname='data.txt'
with open(fname, mode='rb') as f:
    contents=f.read()
    print(type(contents))
    print(contents)
    print(contents.decode('utf16'))

#NFC AND NFD
#stapping
#we remove white space by using white space
s='   Hello world    '
print(s.strip())

s='   Hello world    '
print(s.lstrip())   #remove left side lstrip()

s='   Hello world    '
print(s.rstrip())   #remove right side rstrip()

#character stripping
s='--------Hello world==============='
print(s.strip('-'))

s='--------Hello world==============='
print(s.strip('='))

s='--------Hello world==============='
print(s.strip('-='))

#replace
s='hello world'
s.replace(' ','') #replace this with no space

import re
re.sub('\s+',' ',s)
#aligning the text string
text='Hello World'
text.ljust(20)
text.rjust(20)
text.center(20)

#it allow the optional character
text='Hello World'
text.ljust(20,'-')
text.rjust(20,'=')
text.center(20,'*')

format(text,'>20')  #shift to right side
format(text,'<20')  #text shift to left side
format(text,'^20') #text shift to center by 20 character

#here you can add character to fill the
#as above but if you want to include as function
#character
format(text,'=>20s')
format(text,'=<20s')
format(text,'*^20s')

'{:>10s}{:>10s}'.format('Hello',' World')

#imp in graphics
x=1.23
format(x,'>10')
format(x,'^10,2f')

parts=['Is','Chicago','Not','chicago?']
' '.join(parts)         #it create the sentence

','.join(parts)
' .'.join(parts)
''.join(parts)


d1={i:i for i in range(100,160,10)}









