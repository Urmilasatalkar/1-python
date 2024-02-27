# -*- coding: utf-8 -*-
"""
Created on Fri Aug  4 14:11:03 2023

@author: urmii
"""
#######################FILE OP################################################
########################################################################################
import pandas as pd
import numpy as np
df1=pd.read_csv('c:/2-datasets/crime_data.csv')
# iloc##############
print(df1)
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
df2=df1.iloc[[1,3,4]]  #select 1st 2nd 3rd row and all cols
print(df2)
df2=df1.iloc[1:4] #it will give 1st 2nd 3rd row
print(df2)
df2=df1.iloc[:1] #it will give 0th row
print(df2)
df2=df1.iloc[:3] #it will give 1st 2nd row
print(df2)
df2=df1.iloc[-1:] #it will give last row
print(df2)
df2=df1.iloc[-3:] #it will give last -1 and -2 row means last 2 row
print(df2)
df2=df1.iloc[::2] #it will give all row and all col increament by 2
print(df2)
#drop#############
df1=df1.drop(['Murder'],axis=1)
print(df1)
df1=df1.drop(['Murder'])  #"['Fee'] not found in axis"-----> without giving an axis
print(df1)
df1=df1.drop(labels=['Murder'],axis=1)
print(df1)
df1=df1.drop(columns=['Murder'],axis=1)
print(df1)
df1=df1.drop(df1.columns[1],axis=1)
print(df1)
#using inplace=True  #we want original dataframe in use as that time we use inplace=True
df1.drop(df1.columns[1],axis=1,inplace=True)  #without creating a new instance we can directly use the original dataframe
print(df1)
df2=df1.drop(['Murder','Rape'],axis=1)  #drop more than one col
print(df2)
#drop more than one col usinf index
df2=df1.drop(df1.columns[[0,1]],axis=1)
print(df2)
#drop col from list of cols by name
listcol=['Murder','Rape']
df2=df1.drop(listcol,axis=1)
print(df2)
#drop cols from list of daatframes
df1.drop(df1.columns[1],axis=1,inplace=True)  #without creating a new instance we can directly use the original dataframe
print(df1)
#LOC####################
df2=df1.loc[0]
print(df2)
df2=df1.loc[[0,1,5]]   #row oth 2nd and 4th are getting selected
print(df2)
df2=df1.loc[0:5]  # r2 r3 r4 r5 selected last rows r5 also get selected
print(df2)
df2=df1.loc[0:10:2] #r2 r4 selected
print(df2)
df1=df1.drop(range(0,2))   #row0 and row1 get deleted
print(df1)
df2=df1.rename({'Murder':'A1'},axis=1)
print(df2)
#######################################################################################
import pandas as pd
import numpy as np
df1=pd.read_csv('c:/2-datasets/bank_data.csv')
print(df1)
#ILOC##################
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
df2=df1.iloc[[1,3,4]]  #select 1st 2nd 3rd row and all cols
print(df2)
df2=df1.iloc[1:4] #it will give 1st 2nd 3rd row
print(df2)
df2=df1.iloc[:1] #it will give 0th row
print(df2)
df2=df1.iloc[:3] #it will give 1st 2nd row
print(df2)
df2=df1.iloc[-1:] #it will give last row
print(df2)
df2=df1.iloc[-3:] #it will give last -1 and -2 row means last 2 row
print(df2)
df2=df1.iloc[::2] #it will give all row and all col increament by 2
print(df2)
#DROP###########################
df1=df1.drop(['age'],axis=1)
print(df1)
df1=df1.drop(['age'])  #"['Fee'] not found in axis"-----> without giving an axis
print(df1)
df1=df1.drop(labels=['age'],axis=1)
print(df1)
df1=df1.drop(columns=['loan'],axis=1)
print(df1)
df1=df1.drop(df1.columns[1],axis=1)
print(df1)
#using inplace=True  #we want original dataframe in use as that time we use inplace=True
df1.drop(df1.columns[1],axis=1,inplace=True)  #without creating a new instance we can directly use the original dataframe
print(df1)
df2=df1.drop(['age','loan'],axis=1)  #drop more than one col
print(df2)
#drop more than one col usinf index
df2=df1.drop(df1.columns[[0,1]],axis=1)
print(df2)
#drop col from list of cols by name
listcol=['age','loan']
df2=df1.drop(listcol,axis=1)
print(df2)
#drop cols from list of daatframes
df1.drop(df1.columns[1],axis=1,inplace=True)  #without creating a new instance we can directly use the original dataframe
print(df1)
#LOC#########################
df2=df1.loc[0]
print(df2)
df2=df1.loc[[0,1,5]]   #row oth 2nd and 4th are getting selected
print(df2)
df2=df1.loc[0:5]  # r2 r3 r4 r5 selected last rows r5 also get selected
print(df2)
df2=df1.loc[0:10:2] #r2 r4 selected
print(df2)
df2=df1.drop(range(0,2))   #row0 and row1 get deleted
print(df2)
df2=df1.rename({'age':'A1','balance':'B2'},axis=1)
print(df2)
########################################################################################
import pandas as pd
import numpy as np
df1=pd.read_csv('c:/2-datasets/loan.csv')
print(df1)
#ILOC######################
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
df2=df1.iloc[[1,3,4]]  #select 1st 2nd 3rd row and all cols
print(df2)
df2=df1.iloc[1:4] #it will give 1st 2nd 3rd row
print(df2)
df2=df1.iloc[:1] #it will give 0th row
print(df2)
df2=df1.iloc[:3] #it will give 1st 2nd row
print(df2)
df2=df1.iloc[-1:] #it will give last row
print(df2)
df2=df1.iloc[-3:] #it will give last -1 and -2 row means last 2 row
print(df2)
df2=df1.iloc[::2] #it will give all row and all col increament by 2
print(df2)
#DROP#################################
df1=df1.drop(['id'],axis=1)
print(df1)
df1=df1.drop(['grade'])  #"['Fee'] not found in axis"-----> without giving an axis
print(df1)
df1=df1.drop(labels=['id'],axis=1)
print(df1)
df1=df1.drop(columns=['grade'],axis=1)
print(df1)
df1=df1.drop(df1.columns[1],axis=1)
print(df1)
#using inplace=True  #we want original dataframe in use as that time we use inplace=True
df1.drop(df1.columns[1],axis=1,inplace=True)  #without creating a new instance we can directly use the original dataframe
print(df1)
df2=df1.drop(['id','grade'],axis=1)  #drop more than one col
print(df2)
#drop more than one col usinf index
df2=df1.drop(df1.columns[[0,1]],axis=1)
print(df2)
#drop col from list of cols by name
listcol=['id','grade']
df2=df1.drop(listcol,axis=1)
print(df2)
#drop cols from list of daatframes
df1.drop(df1.columns[1],axis=1,inplace=True)  #without creating a new instance we can directly use the original dataframe
print(df1)
#LOC###############
df2=df1.loc[0]
print(df2)
df2=df1.loc[[0,1,5]]   #row oth 2nd and 4th are getting selected
print(df2)
df2=df1.loc[0:5]  # r2 r3 r4 r5 selected last rows r5 also get selected
print(df2)
df2=df1.loc[0:10:2] #r2 r4 selected
print(df2)
df2=df1.drop(range(0,2))   #row0 and row1 get deleted
print(df2)
df2=df1.rename({'id':'A1'},axis=1)
print(df2)
