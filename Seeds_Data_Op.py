# -*- coding: utf-8 -*-
"""
Created on Tue Aug  8 16:31:13 2023

@author: urmii
"""

import pandas as pd
import numpy as np
f=pd.read_csv('c:/2-datasets/Seeds_data.csv')
df=pd.DataFrame(f)
df

#------------------------------QUERY-------------------------------------
df1=df.query("Type==1")
df1
df1=df.query("Type!=1")
df1
#---------------------------------ADD new col-------------------------------
df.shape
for i in range(0,211):
    df['Discount']=2  #col name=values
    print(df)

#--------------------------------------find total rows and cols---------------------------------
rows_count=len(df.index)  #row count  #210
rows_count
print("Total number of rows:" +str(rows_count))
row_count=len(df.axes[0])  #row count  #210
row_count
col_count=len(df.axes[1]) #col count  #9
col_count
print("Total number of rows:" +str(col_count))
row_count=df.shape[0]   #row count   #210
row_count
col_count=df.shape[1]  #col count    #9
col_count

#---------------------------------------Display Summary------------------------
df.describe()
#Area  Perimeter   ...  len_ker_grove        Type
#count  210.000000  210.000000  ...     210.000000  210.000000
##mean    14.847524   14.559286  ...       5.408071    2.000000
#std      2.909699    1.305959  ...       0.491480    0.818448
#min     10.590000   12.410000  ...       4.519000    1.000000
#25%     12.270000   13.450000  ...       5.045000    1.000000
#50%     14.355000   14.320000  ...       5.223000    2.000000
#75%     17.305000   15.715000  ...       5.877000    3.000000
#max     21.180000   17.250000  ...       6.550000    3.000000
df.info()
#Data columns (total 8 columns):
 #   Column           Non-Null Count  Dtype  
#---  ------           --------------  -----  
 #0   Area             210 non-null    float64
 #1   Perimeter        210 non-null    float64
 #2   Compactness      210 non-null    float64
 #3   length           210 non-null    float64
 #4   Width            210 non-null    float64
 #5   Assymetry_coeff  210 non-null    float64
 #6   len_ker_grove    210 non-null    float64
 #7   Type             210 non-null    int64  
#dtypes: float64(7), int64(1)
#------------------------------------- print specific row-----------------------------
df.iloc[0:50]
df.iloc[6:60]
df.iloc[1:50:2]

#---------------------------------------Rename------------------------------
df2=df.rename({'Area':'A1'},axis=1)
print(df2)

#-------------------------------------Drop-------------------------------
df1=df.drop(['Area'],axis=1)
print(df1)
df1=df.drop(['Area'])  #"['Fee'] not found in axis"-----> without giving an axis
print(df1)
df1=df.drop(labels=['Perimeter'],axis=1)
print(df1)
df1=df.drop(columns=['Perimeter'],axis=1)
print(df1)
df1=df.drop(df1.columns[1],axis=1)
print(df1)
#-----------------------------iloc/loc-----------------------------------
df2=df1.iloc[1:4,0:2]
print(df2)
df2=df1.iloc[:,0:2] #first : return all rows after comma it will return cols from 0th and 1st col
print(df2)
df2=df1.iloc[0:2,:] #first : return all cols after comma it will return rows from 0th and 1st col
print(df2)
df2=df1.iloc[1:3,1:3] #first : return all cols after comma it will return rows from 0th and 1st col
print(df2)
df2=df1.iloc[2] #select row by index
print(df2)
#-------------------------------------ADD ROW----------------------------
#adding new row in dataframe
df.loc['totor']=[12,234,123,2.11,4.22,1,2,4]
df

df.columns
def add_5(x):
    x=x+5
    return x
df1=df['Area'].apply(add_5)
print(df1)

df[['Area','Perimeter']]=df[['Area','perimeter']].apply(add_5)
print(df)

#using lambda function
df2=df.apply(lambda x:x+5)
df2
df2=df['Area'].apply(lambda x:x+5)
df2
df2=df[['Area','Perimeter']].apply(lambda x:x+5)
df2

#using transform method
def add_5(x):
    x=x+10
    return x
df2=df['Area'].transform(add_5)
print(df2)

df2=df[['Area','Perimeter']].transform(add_5)
df2

#----------------------------------------using map()
def add_5(x):
    x=x+10
    return x

#------------------------------MAP()
df2=df['Area'].map(lambda SepalLengthCm:SepalLengthCm/5)
print(df2)


col_headers=list(df.columns.values)
print("Column headers",col_headers)

import numpy as np
df['Area']=df['Perimeter'].apply(np.square)
df
df[['Area','Perimeter']]=df[['Area','Perimeter']].apply(np.square)
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
















