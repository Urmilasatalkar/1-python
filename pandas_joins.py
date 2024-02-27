# -*- coding: utf-8 -*-
"""
Created on Wed Aug  9 22:49:49 2023

@author: urmii
"""

import pandas as pd
d={'id':[1,2,3,4],
   'val1':['a','b','c','d']
   }
df1=pd.DataFrame(d)
print(df1)
b={'id':[1,2,9,8],
   'val1':['p','q','r','s']
   }
df2=pd.DataFrame(b)
print(df2)
df3=df1.join(df2,lsuffix="_left",rsuffix="_right")
print(df3)
df3=df1.join(df2,lsuffix="_left",rsuffix="_right",how='left')
print(df3)
df3=df1.join(df2,lsuffix="_left",rsuffix="_right",how='right')
print(df3)
