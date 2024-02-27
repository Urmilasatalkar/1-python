# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 10:44:20 2023

@author: urmii
"""

pt=str(input("Enter plain text:"))
key='ldrp'
for i in pt:
    for j in pt:
        print(i)
        print(j+1)
l1=[]
l2=[]
for i in pt:
    l1.append(i)
for j in pt:
    l2.append(j+1)
print(l1)
print(l2)    

def form_string_pairs(input_string):
    pairs = [(input_string[i], input_string[i + 1])for i in range(0, len(input_string) - 1, 2)]
    if len(input_string) % 2 == 1:
        pairs.append((input_string[-1], 'z'))
    return pairs


input_string = input('Enter plain text: ')
pairs = form_string_pairs(input_string)
print("String pairs:", pairs)

def form_string_pairs(input_string):
    pairs = [(input_string[i],input_string[i + 1]) for i in range(0, len(input_string) - 1, 2)]
    if len(input_string) % 2 == 1:
        pairs.append((input_string[-1], 'z'))

    updated_pairs = []
    for i, j in pairs:
        if i == j:
            updated_pairs.append((i, 'x'))
            #updated_pairs.append((char1, char2))
        else:
            updated_pairs.append((i, j))
    
    return updated_pairs
input_string= input('Enter plain text: ')
pairs = form_string_pairs(input_string)
print("String pairs:", pairs)

inp=input("Enter text")
key='ldrp'
i=0
list1=[]
while(i<len(inp)):
    if i+1 < len(inp):
        if inp[i] != inp[i+1]:
            ele = inp[i]+inp[i+1]
            i=i+2
        else:
            ele = inp[i]+'x'
            i =i+1
    else:
        ele = inp[i]
        i =i+2
    list1.append(ele)
print(list1)
mat=[[i for i in range(0,5)] for j in range(0,5)]
print(mat)

matrix = [['' for _ in range(5)] for _ in range(5)]
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
letter_index = 0
for i in range(5):
    for j in range(5):
        if letter_index < len(alphabet):
            matrix[i][j] = alphabet[letter_index]
            letter_index += 1
matrix[0][3]='ldrp'
for row in matrix:
    print(' '.join(row))

matrix = [['' for _ in range(5)] for _ in range(5)]
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
key='ldrp'
letter_index = 0
letter_index1 = 0
for char in 'ldrp':
    matrix[0][letter_index] = char
    letter_index += 1
for i in range(5):
    for j in range(5):
        if letter_index < len(key):
            matrix[i][j] =key[letter_index]
            letter_index += 1
        else:
                if letter_index1<j:
                    matrix[i][j] = alphabet[letter_index]
                    letter_index += 1
for row in matrix:
    print(' '.join(row))

def toLowerCase(text):
    return text.lower()

def removeSpaces(text):
    return text.replace(" ", "")

def diagraph(text):
    diagraph = []
    for i in range(1, len(text), 2):
        if i + 1 < len(text) and text[i] == text[i + 1]:
            diagraph.append(text[i] + 'x')
        else:
            diagraph.append(text[i - 1:i + 1])
    if len(text) % 2 == 1:
        diagraph.append(text[-1] + 'x')
    return diagraph

def generateKeyTable(key):
    key = removeSpaces(toLowerCase(key))
    alphabet = 'abcdefghiklmnopqrstuvwxyz'
    key = ''.join(sorted(set(key), key=key.index))
    keytable = [list(key[i:i+5]) for i in range(0, len(key), 5)]
    for char in alphabet:
        if char not in key and char != 'j':
            keytable.append(char)
    return keytable

def findPosition(keytable, char):
    for i in range(5):
        for j in range(5):
            if keytable[i][j] == char:
                return (i, j)
    # If char is not found in the keytable, you can handle it here, e.g., return (-1, -1)
    return (-1, -1)


def encryptPair(keytable, pair):
    char1, char2 = pair
    row1, col1 = findPosition(keytable, char1)
    row2, col2 = findPosition(keytable, char2)
    if row1 == row2:
        return keytable[row1][(col1 + 1) % 5], keytable[row2][(col2 + 1) % 5]
    elif col1 == col2:
        return keytable[(row1 + 1) % 5][col1], keytable[(row2 + 1) % 5][col2]
    else:
        return keytable[row1][col2], keytable[row2][col1]

def encrypt(text, key):
    keytable = generateKeyTable(key)
    pairs = diagraph(removeSpaces(toLowerCase(text)))
    ciphertext = ""
    for pair in pairs:
        char1, char2 = encryptPair(keytable, pair)
        ciphertext += char1 + char2
    return ciphertext

text_plain = 'communicate'
key = "computer"
ciphertext = encrypt(text_plain, key)
hprint("CipherText:", ciphertext)








