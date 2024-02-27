# -*- coding: utf-8 -*-
"""
Created on Thu Aug 10 00:00:28 2023

@author: urmii
"""

####################iloc############################################
import pandas as pd
import numpy as np
technologies=({'courses':['spark','pyspark','hadoop','python','sql','pandas'],
              'Fee':[2000,1200,23400,2400,1455,1256],
              'Duration':['30days','40days','20days','80days','10days','1200days'],
              'Discount':[10,20,30,40,50,60]})
df=pd.DataFrame(technologies)
row_labels=['r0','r1','r2','r3','r4','r5']
df=pd.DataFrame(technologies,index=row_labels)
print(df)
#df.iloc[startrow:endrow ,startcol:endcol]
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
df2=df.iloc[[1,3,4]]  #select 1st 2nd 3rd row and all cols
print(df2)
df2=df.iloc[1:4] #it will give 1st 2nd 3rd row
print(df2)
df2=df.iloc[:1] #it will give 0th row
print(df2)
df2=df.iloc[:3] #it will give 1st 2nd row
print(df2)
df2=df.iloc[-1:] #it will give last row
print(df2)
df2=df.iloc[-3:] #it will give last -1 and -2 row means last 2 row
print(df2)
df2=df.iloc[::2] #it will give all row and all col increament by 2
print(df2)
#################################################
#using loc
#################################LOC##################################
import pandas as pd
import numpy as np
technologies=({'courses':['spark','pyspark','hadoop','python','sql','pandas'],
              'Fee':[2000,1200,23400,2400,1455,1256],
              'Duration':['30days','40days','20days','80days','10days','1200days'],
              'Discount':[10,20,30,40,50,60]})
df=pd.DataFrame(technologies)
row_labels=['r0','r1','r2','r3','r4','r5']
df=pd.DataFrame(technologies,index=row_labels)
#select row index by lebels
print(df)
df2=df.loc['r2']
print(df2)
df2=df.loc[['r0','r2','r4']]   #row oth 2nd and 4th are getting selected
print(df2)
df2=df.loc['r2':'r5']  # r2 r3 r4 r5 selected last rows r5 also get selected
print(df2)
df2=df.loc['r2':'r5':2] #r2 r4 selected
print(df2)
#df.loc[:,start:stop:step]
#select multiple cols
import pandas as pd
import numpy as np
technologies=({'courses':['spark','pyspark','hadoop','python','sql','pandas'],
              'Fee':[2000,1200,23400,2400,1455,1256],
              'Duration':['30days','40days','20days','80days','10days','1200days'],
              'Discount':[10,20,30,40,50,60]})
df=pd.DataFrame(technologies)
row_labels=['r0','r1','r2','r3','r4','r5']
df=pd.DataFrame(technologies,index=row_labels)
df2=df.loc[:,['courses','Fee','Duration']]
print(df2)
df2=df.loc[:,'Duraton':]
print(df2)