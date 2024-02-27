# -*- coding: utf-8 -*-
"""
Created on Wed Aug  9 16:43:39 2023

@author: urmii
"""
#------------------------------------------9-aug op on file----------------------------
import pandas as pd
df=pd.read_csv('c:/2-datasets/Iris.csv')
df
df.columns
def add_5(x):
    x=x+5
    return x
df1=df['SepalLengthCm'].apply(add_5)
print(df1)

df[['SepalLengthCm','SepalWidthCm']]=df[['SepalLengthCm','SepalWidthCm']].apply(add_5)
print(df)

#using lambda function
df2=df.apply(lambda x:x+5)
df2
df2=df['SepalLengthCm'].apply(lambda x:x+5)
df2
df2=df[['SepalLengthCm','SepalWidthCm']].apply(lambda x:x+5)
df2

#using transform method
def add_5(x):
    x=x+10
    return x
df2=df['SepalLengthCm'].transform(add_5)
print(df2)

df2=df[['SepalLengthCm','SepalWidthCm']].transform(add_5)
df2

#----------------------------------------using map()----------------------------
def add_5(x):
    x=x+10
    return x

#------------------------------MAP()------------------------------------------
df2=df['SepalLengthCm'].map(lambda SepalLengthCm:SepalLengthCm/5)
print(df2)

#------------------------------------groupBy()
df2=df.groupby(['Species']).sum()
print(df2)

col_headers=list(df.columns.values)
print("Column headers",col_headers)

import numpy as np
df['SepalWidthCm']=df['SepalWidthCm'].apply(np.square)
df
df[['SepalLengthCm','SepalWidthCm']]=df[['SepalLengthCm','SepalWidthCm']].apply(np.square)
df
#==============================Sample==============================================
df1=df.sample(frac=1)
print(df1)
df1=df.sample(frac=0.5)
print(df1)
df1=df.sample(frac=0.5).reset_index()
print(df1)
df1=df.sample(frac=1).reset_index(drop=True)  #it drop the shuffle index
print(df1)

df2=df.iloc[1:4,0:2]
print(df2)
df2=df.iloc[:,0:2] #first : return all rows after comma it will return cols from 0th and 1st col
print(df2)
df2=df.iloc[0:2,:] #first : return all cols after comma it will return rows from 0th and 1st col
print(df2)
df2=df.iloc[1:3,1:3] #first : return all cols after comma it will return rows from 0th and 1st col
print(df2)
df2=df.iloc[2] #select row by index
print(df2)

df1=df.drop(labels=['Id'],axis=1)
print(df)
df1=df.drop(columns=['Species'],axis=1)
print(df)
df1=df.drop(df.columns[1],axis=1)
print(df)

df2=df.loc[0]
print(df2)
df2=df.loc[[0,1,5]]   #row oth 2nd and 4th are getting selected
print(df2)
df2=df.loc[0:5]  # r2 r3 r4 r5 selected last rows r5 also get selected
print(df2)
