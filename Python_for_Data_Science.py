# -*- coding: utf-8 -*-
"""
Created on Wed Aug  2 09:39:49 2023

@author: urmii
"""

#---------------------------series-----------------------------
import pandas as pd
song2=pd.Series([123,12,345,12],name='counts')
song2.index   #by default it takes index as integer

#make index as string
import pandas as pd
song3=pd.Series([123,12,345,12],name='counts',index=['A','B','C','D'])
song3.index   #by default it takes index as integer
song3       #checking the whole series

#absolute path
import pandas as pd
f1=pd.read_csv('C:/1-python/age.csv')
f1
#relative path
import pandas as pd
f1=pd.read_csv('age.csv')
f1

#for excel file
#absolute path
import pandas as pd
f1=pd.read_excel('C:/1-python/Bahaman.xlsx')
f1
#relative path
import pandas as pd
f1=pd.read_excel('Bahaman.xlsx')
f1
##########################################
#start working on series
import numpy as np
numpy_ser=np.array([1,2,3,4,5])
song3[1]    #3
numpy_ser[3]
song3.mean()    #123.0
numpy_ser.mean()    #3.0

################################
#pandas series
#series can allow duplicate index
#series can allow string as an integer
#length of values should be same as index
george=pd.Series([12,1,34,4],index=[1200,'1200','1200','1489'],name='George Songs')
george
george['1200'] 
george[1200]  #it get print both indexes and its integer
for i in george:
    print(i)

#updating values in series
george['1200']=123
george['1200']

#Deleting
s=pd.Series([1,2,3,4],index=[3,4,5,6])
del s[4]
s

s=pd.Series([1,2,3,4],index=[3,4,5,6])
del s
#convet types
# string use.astype(str)
import pandas as pd
george=pd.Series([300,500,600,400],index=[1200,1300,1400,1500],name='George Songs')
george.dtypes
pd.to_numeric(george.apply(str))
pd.to_numeric(george.astype(str),errors="coerce")   #it execute the series not giving an error

# to avoid the error we need to fill none 
#some techniques to remove none
george.fillna(-1)
george.dtypes

#NAN can be deopped from    #it directly delete that row
#the series using dropna
george.dropna()

#append, combining and joining two series

#appending one series into another
george1=pd.Series([200,600,300,500],index=[10,20,30,40],name='George1 Songs')
geo=george.append(george1)

#plotting series
import matplotlib.pyplot as plt
fig=plt.figure()
george.plot()
plt.legend()
###########################
fig=plt.figure()
george.plot(kind='bar',color='g')
george1.plot(kind='bar',color='y')
plt.legend()

#generate random number histogram
import numpy as np
data=pd.Series(np.random.randn(500),name='500 Random')
fig=plt.figure()
ax=fig.add_subplot(111)
data.hist()

# upgrade to pandas commands
#conda install update pandas==2.0.3
#conda install -c anaconda pandas

#to check version of pandas
import pandas as pd
pd.__version__

#create using constructor
#create pandas dataframes from list
import pandas as pd
technologies=[['spark',20000,'30days'],['panda',20000,'40days']]
df=pd.DataFrame(technologies)
print(df)

#pass col_names and rows name to dataframes
col_names=['Courses','Fee','Duration']
row_names=['A','B']
df=pd.DataFrame(technologies,columns=col_names,index=row_names)
print(df)
df.dtypes

#dataframes using dictionary
import pandas as pd
technologies={'courses':['spark','pyspark','hadoop','python','sql','pandas'],
              'Fee':[2000,1200,23400,2400,1455,1256],
              'Duration':['30days','40days','20days','80days','10days','1200days'],
              'Discount':[1,2,3,4,5,67]}
df2=pd.DataFrame(technologies)
print(df2)
print(df2.dtypes)

#convert data all data types to best possible types
df2=df2.convert_dtypes()
print(df2.dtypes)

#change all col to same data types
df=df.astype(str)
print(df.dtypes)

#change type for one or more col
df=df.astype({"Fee":int,"Discount":float})
print(df.dtypes)

#convert data types for all col in list
df=pd.DataFrame(technologies)
df.dtypes
cols=['Fee','Discount']
df[cols]=df[cols].astype(float)
df.dtypes

#Ignore Errors
#courses is string type but by using error we ignore the error
df=df.astype({'courses':int},errors='ignore')
df.dtypes

##############################################################
#converting dataframes into csv
import pandas as pd
technologies={'courses':['spark','pyspark','hadoop','python','sql','pandas'],
              'Fee':[2000,1200,23400,2400,1455,1256],
              'Duration':['30days','40days','20days','80days','10days','1200days'],
              'Discount':[1,2,3,4,5,67]}
df2=pd.DataFrame(technologies)
df2.to_csv('Data.csv')
df2=pd.read_csv('Data.csv')

#create dataframe with none/null to work exampples
#EDA Exploratory data analysis
import pandas as pd
import numpy as np
technologies=({'courses':['spark','pyspark','hadoop','python','sql','pandas'],
              'Fee':[2000,1200,23400,2400,1455,1256],
              'Duration':['30days','40days','20days','80days','10days','1200days'],
              'Discount':[10,20,30,40,50,60]})
df=pd.DataFrame(technologies)
row_labels=['r0','r1','r2','r3','r4','r5']
df=pd.DataFrame(technologies,index=row_labels)
#############################################################
#dropping rows
df1=df.drop(['r1','r2'])   # drop the row by lebels
print(df1)
df1=df.drop(df.index[1])
df1
df1=df.drop(df.index[[1,4]])
df1
df1=df.drop(df.index[2:])
print(df1)
df=pd.DataFrame(technologies)
df1=df.drop(0)   #row0 will get deleted
df1
df=pd.DataFrame(technologies)
df1=df.drop([0,3])  # row0 and row3 will get deleted
df1
df1=df.drop(range(0,2))   #row0 and row1 get deleted
df1

############################################################
#dropping columns
import pandas as pd
import numpy as np
technologies=({'courses':['spark','pyspark','hadoop','python','sql','pandas'],
              'Fee':[2000,1200,23400,2400,1455,1256],
              'Duration':['30days','40days','20days','80days','10days','1200days'],
              'Discount':[10,20,30,40,50,60]})
df=pd.DataFrame(technologies)
print(df)
df1=df.drop(['Fee'],axis=1)
print(df1)
df1=df.drop(['Fee'])  #"['Fee'] not found in axis"-----> without giving an axis
print(df1)
df1=df.drop(labels=['Fee'],axis=1)
print(df1)
df1=df.drop(columns=['Fee'],axis=1)
print(df1)
df1=df.drop(df.columns[1],axis=1)
print(df1)
#using inplace=True  #we want original dataframe in use as that time we use inplace=True
df.drop(df.columns[1],axis=1,inplace=True)  #without creating a new instance we can directly use the original dataframe
print(df)
df=pd.DataFrame(technologies)
print(df)
df2=df.drop(['courses','Fee'],axis=1)  #drop more than one col
print(df2)
df=pd.DataFrame(technologies)
#drop more than one col usinf index
df2=df.drop(df.columns[[0,1]],axis=1)
print(df2)
#drop col from list of cols by name
df=pd.DataFrame(technologies)
listcol=['courses','Fee']
df2=df.drop(listcol,axis=1)
print(df2)
#drop cols from list of daatframes
df.drop(df.columns[1],axis=1,inplace=True)  #without creating a new instance we can directly use the original dataframe
print(df)
##############################################################
#using loc and iloc-------------------------------------------


###############################################
#dataframes properties
df.shape    #(6,4)  #(row,col)
df.size     #24
df.columns  #Index(['courses', 'Fee', 'Duration', 'Discount'], dtype='object')
df.columns.values  #array(['courses', 'Fee', 'Duration', 'Discount'], dtype=object)
df.index    #Index(['r0', 'r1', 'r2', 'r3', 'r4', 'r5'], dtype='object')
df.dtypes           #courses       object
                    # Fee          int64
                    # Duration     object
                    # Discount     int64
                    # dtype: object
########################################################
#accessing one col content
df['Fee']
df.Fee
#access two or more col
df[['Fee','Discount']]

#select certain rows and assign it to another dataframes
df2=df[3:]
print(df2)
df2=df[1:3]
print(df2)

#accssing certain cell from a col
df['Duration'][3]


#Substracting specific values from col
df['Fee']=df['Fee']-500
df['Fee']
print(df)
#pandas to minipulate dataframes
#Describe dataframes
#describe dataframe for all numberic cols
df.describe()

#renaming
#rename()-> renames pandas dataframe cols
df.columns=['A','B','C','D']
print(df)
df2=df.rename({'A':'c1','B':'c2'},axis=1)
df2=df.rename({'C':'c3','D':'c4'},axis='columns')
df2=df.rename(columns={'A':'c1','B':'c2'})
print(df2)

#-----------------------------------------------------------------------------------
#Create Series
import pandas as pd
ds=pd.Series([2,3,4,5,6,6])
print(ds)

#Write a python program to convert a panda mudule series 
#to python list and it's type
import pandas as pd
ds=pd.Series([2,3,4,5,6])
print(ds)
print(ds.dtypes)    #dtype: int64
print("Convert series into list:...")
print(ds.tolist())     #[2, 3, 4, 5, 6]
print(type(ds))       #<class 'pandas.core.series.Series'>

#write a python program to add,sub,mul,divide
import pandas as pd
ds1=pd.Series([2,3,4,5,7])
ds2=pd.Series([4,5,6,7,8])
print("Addition of two Series:\n",ds1+ds2)
print("\nSubstraction of two series:\n",ds2-ds1)
print("\nMultiplication:\n",ds1*ds2)
print("\nDivide:\n",ds1/ds2)

#write a program to compare series element
import pandas as pd
ds1=pd.Series([2,5,7,5,9])
ds2=pd.Series([4,5,6,7,8])
print("Equals:\n")
print(ds1==ds2)
print("Greater than:")
print(ds1>ds2)
print("Less than")
print(ds1<ds2)

#write a python program to convert dict to sample series
import pandas as pd
ds3={'a':100,'b':200,'c':300,'d':500,'e':600}
print("Original dict:")
print(ds3)
new_series=pd.Series(ds3)
print("Converted into Series:\n")
print(new_series)

#write a python program to convert a numpy array to a pandas series
import pandas as pd
import numpy as np
ny=np.array([10,20,30,40,50])
print(ny)
new_series=pd.Series(ny)
print(new_series)

#write a python program to change data types of a given data types
import pandas as pd
ds1=pd.Series([2,5,7,5,9,'python','html'])
print(ds1.dtypes)
print(type(ds1))
s2=pd.to_numeric(ds1,errors="coerce")
print(s2)

#write a python program to convert the first col of a dataframe as a series
import pandas as pd
d={'col1':[1,2,3,4,5],
   'col2':[6,7,8,9,0],
   'col3':[1,2,3,4,5]
   }
ds4=pd.DataFrame(data=d)
print(ds4)
s1=ds4.iloc[:,0:2]
print(s1)
s1=ds4.iloc[:,0]
print(type(s1))
print(s1)            
#operate on dataframe
def add3(x):
    return x+3
df=ds4.apply(add3)
df
df1=ds4['col1'].apply(add3)
df1
df1=(ds4.col1).apply(add3)
df1
ds4[['col1','col2']]=ds4[['col1','col2']].apply(add3)  #all col will print
ds4
ds4[['col1','col2']]=ds4[['col1','col2']].apply(add3)  #all col will print
ds4
##############################################
import pandas as pd
s=pd.Series([['red','green','black'],
            ['yellow','pink','orange'],
            ['purple','white','peach']])
print(s)
#s=s.apply(pd.Series).stack().reset_index(drop=True)
print(s)
###########################################
import pandas as pd
s=pd.Series([['red','green','black'],
            ['yellow','pink','orange'],
            ['purple','white','peach']])
print(s)
s1=s.apply(pd.Series)
s2=s1.stack()
s3=s2.reset_index(drop=True)
print(s3)

#write a python program ro add some data in the series 
###################################################
import pandas as pd
s=pd.Series([100,200,300,'python','html','CSS',500,700])
new_s=pd.concat([s,pd.Series([500,'php'])],ignore_index=True)
print(new_s)

#write a program to sort a given Series
import pandas as pd
s=pd.Series(['50','10','100','200','300','python','html','CSS','500','700','111'])
new_s=pd.Series(s).sort_values()
print(new_s)

#######################################################
#write a python program to change the order of index 
#of a given series
import pandas as pd
s=pd.Series(data=[1,2,3,4,5],index=['A','B','C','D','E'])
print(s)
s=s.reindex(index=['B','A','C','D','E'])
print(s)
print(s.dtypes)

#----------------------------------8-aug-23---------------------------------------------
import pandas as pd
technologies={'courses':['spark','pyspark','hadoop','python','sql','pandas'],
              'Fee':[2000,1200,23400,2400,1455,1256],
              'Duration':['30days','40days','20days','80days','10days','1200days'],
              'Discount':[1,2,3,4,5,67]}
df2=pd.DataFrame(technologies)


#pandas.dataframe.query() by ex
#query all rows with courses equals spark
df3=df2.query("courses=='spark'")
print(df3)

df3=df2.query("courses!='spark'")
print(df3)
#add new col into dataframe
tutors=['ram','shayam','ghansham','radha','krishana','ganesh']
df3=df2.assign(TutorAssigned=tutors)   #col name=values
print(df3)

MNCCamp=['TATA','TCS','KPIT','WINJIT','GOOGLE','AMAZON']
df3=df2.assign(MNC=MNCCamp,tutors=tutors)
print(df3)

#derive new col from existing col
df3=df2.assign(Discount_percent=lambda x:x.Fee * x.Discount/100)
print(df3)

#append col to existing pandas dataframe
#add new col to existing datframe
df3['MNCCompany']=MNCCamp
print(df3)

#add new col at the specific location
df2.insert(0,'tutors',tutors)
print(df2)
df2.insert(2,'Tutors',tutors)
print(df2)

#to get number of cols from datafrme
rows_count=len(df2.index)  #row count  #6
rows_count
row_count=len(df2.axes[0])  #row count  #6
row_count
col_count=len(df2.axes[1]) #col count  #4
col_count
row_count=df2.shape[0]   #row count   #6
row_count
col_count=df2.shape[1]  #col count    #4
col_count

#write pandas program to create dataframe from dict
import pandas as pd
num={'x':[1,2,3,4,5],
     'y':[5,6,7,8,9],
     'z':[12,33,34,45,67] 
     }
df=pd.DataFrame(num)
print(df)

sanjivani={'Department':['Comp','IT','Mech','CIVIL'],
           'Faculty':['Sangale sir','Kale sir','Bodhe sir','gunjal sir']
           }
df=pd.DataFrame(sanjivani)
print(df)

#create a dataframe using dict with nan value
import pandas as pd
import numpy as np
exam_data={'Name':['Ram','Shayam','Yogesh','Sita','Gita','Mahesh','Shiv'],
           'Score':[12,34,56,None,45,12,56],
           'Attempts':[1,2,5,np.nan,2,3,5],
           'Qualify':['yes','no','yes',None,'yes','no','no'],
           }
Labels=['a','b','c','d','e','f','g']
df=pd.DataFrame(exam_data,index=Labels)
print(df)

df2=len(df.index)
print(df2)
df2=len(df.columns)
print(df2)

#write pandas profram to display summary of 
#data
df.describe()   #it only take int data
print(df.info())

#write pandas to get first three rows of given data set
print("First three rows:")
df.iloc[0:3]

#write python program to select name and score col from given dataset
print("name and score col:")
df[['Name','Score']]
df2=df.loc[:,['Name','Score']]
print(df2)

#write a pandas program to select the specified col and rows from a 
df2=df.loc['a'::2,['Score','Qualify']]
print(df2)
########
col=[1,3]
df2=df.iloc[0::2,col]
print(df2)
########

###############################
import pandas as pd
import numpy as np
exam_data={'Name':['Ram','Shayam','Yogesh','Sita','Gita','Mahesh','Shiv'],
           'Score':[18,19,56,None,45,12,56],
           'Attempts':[1,2,5,np.nan,2,3,5],
           'Qualify':['yes','no','yes',None,'yes','no','no'],
           }
Labels=['a','b','c','d','e','f','g']
df=pd.DataFrame(exam_data,index=Labels)
print(df)
#write a python program to select row where number of attempt in examination 
#is greater than two
print(df[df['Attempts']>2])  #1st df[attempts] take attempt 
                            #2nd df checking the condition
df2=df.loc[df.Attempts>2]  
print(df2)                          
#Name  Score  Attempts Qualify
#c  Yogesh   56.0       5.0     yes
#f  Mahesh   12.0       3.0      no
#g    Shiv   56.0       5.0      no                            



#write a python program to count the number of rows and cols from dataframe
df1=len(df.index)   #it gives no of rows
print(df1)          #it gives no of cols
print("Total number of rows:" +str(df1))
df1=len(df.columns)
print(df1)
print("Total number of rows:" +str(df1))
df1=len(df.axes[0])  #row count     #7
df1
df1=len(df.axes[1]) #col count      #4
df1
df1=df.shape[0]   #row count      #7
df1
df1=df.shape[1]  #col count       #4
df1


#write the pandas program where the score is missing
df1=df.query("Score.isnull()")
print(df1)

df1=(df[df['Score'].isnull()])
df1
df1=df[df['Score']==None]
df1
#write pandas program to select rows betn 12 and 20
df1=(df[df['Score'].between(15,20)])
df1
#write pandas program to select the score wehrer number of attempts is less than 2 and 
#score greater than 15
df2=df.loc[(df.Attempts<2) & (df.Score>15)]  
print(df2)  

df1=(df[(df['Score']>15) & (df['Attempts']<2)])
df1

#write a program to change the scoree in row d to 11.5
df.loc['d','Score']=11.5   #d=row name  Score=Col name
print(df)

#write the search of program to calculate the sum of examination
#attempts by the student
df1=df['Attempts'].sum()
print(df1)

#write pandas program to calc mean of all students score
df1=df['Score'].mean()
print(df1)

#write a search pandas program to append a new row
#'K' to data frame with given values of each col
df.loc['h']=['geeta','12','3','No']
print(df)
df1=len(df.index)
df1

#write a python program to sort the first dataframe first by name in desc order
#and then by socre aesc ordre
import pandas as pd
import numpy as np
exam_data={'Name':['Ram','Shayam','Yogesh','Sita','Gita','Mahesh','Shiv'],
           'Score':[12,34,56,None,45,12,56],
           'Attempts':[1,2,5,np.nan,2,3,5],
           'Qualify':['yes','no','yes',None,'yes','no','no'],
           }
Labels=['a','b','c','d','e','f','g']
df=pd.DataFrame(exam_data,index=Labels)
print(df)
print("Sort the dataframes first name by desc and then score by asec")
df1=df.sort_values(by=['Name','Score'], ascending=[False,True])
df1
df1=df.sort_values(by=['Name'], ascending=[False])
df1
df1=df.sort_values(by=['Score'], ascending=[True])  #NAN at the last
df1

#write a program to replace the qualify col contents the values yes and no with 
#true or false
import pandas as pd
import numpy as np
exam_data={'Name':['Ram','Shayam','Yogesh','Sita','Gita','Mahesh','Shiv'],
           'Score':[12,34,56,None,45,12,56],
           'Attempts':[1,2,5,np.nan,2,3,5],
           'Qualify':['yes','no','yes',None,'yes','no','no'],
           }
Labels=['a','b','c','d','e','f','g']
df=pd.DataFrame(exam_data,index=Labels)
print(df)

df['Qualify']=df['Qualify'].replace('yes','True')
df['Qualify']=df['Qualify'].replace('no','False')
df
df['Qualify']=df['Qualify'].map({'yes':True,'no':False})  #NAN will not replace
print(df)


#write a program to change the name yogesh with rohit in name col
import pandas as pd
import numpy as np
exam_data={'Name':['Ram','Shayam','Yogesh','Sita','Gita','Mahesh','Shiv'],
           'Score':[12,34,56,None,45,12,56],
           'Attempts':[1,2,5,np.nan,2,3,5],
           'Qualify':['yes','no','yes',None,'yes','no','no'],
           }
Labels=['a','b','c','d','e','f','g']
df=pd.DataFrame(exam_data,index=Labels)
print(df)
df['Name'].replace('Yogesh','Rohit')
df['Name']=df['Name'].replace('Yogesh','Rohit')
print(df)

#write a python program to insert a new col in existing dataframe
import pandas as pd
import numpy as np
exam_data={'Name':['Ram','Shayam','Yogesh','Sita','Gita','Mahesh','Shiv'],
           'Score':[12,34,56,None,45,12,56],
           'Attempts':[1,2,5,np.nan,2,3,5],
           'Qualify':['yes','no','yes',None,'yes','no','no'],
           }
Labels=['a','b','c','d','e','f','g']
df=pd.DataFrame(exam_data,index=Labels)
print(df)
color=['red','green','blue','black','pink','orange','purple']
df["Color"]=color
print(df)

#write a pandas program to iterate 
#over rows in a dataframe
import pandas as pd
import numpy as np
exam_data={'Name':['Ram','Shayam','Yogesh','Sita','Gita','Mahesh','Shiv'],
           'Score':[12,34,56,None,45,12,56],
           'Attempts':[1,2,5,np.nan,2,3,5],
           'Qualify':['yes','no','yes',None,'yes','no','no'],
           }
Labels=['a','b','c','d','e','f','g']
df=pd.DataFrame(exam_data,index=Labels)
print(df)
for index,row in df.iterrows():
    print(row['Name'],row["Score"])


#####################################9-aug##############################
import pandas as pd
d={'col1':[1,2,3,4,5],
   'col2':[6,7,8,9,0],
   'col3':[1,2,3,4,5]
   }
ds4=pd.DataFrame(data=d)
def add3(x):
    return x+3
df=ds4.apply(add3)
df
df1=ds4['col1'].apply(add3)
df1
df1=(ds4.col1).apply(add3)
df1
ds4[['col1','col2']]=ds4[['col1','col2']].apply(add3)  #all col will print
ds4
df1=ds4[['col1','col2']].apply(add3)  #all col will print
df1

#lambda
df2=ds4.apply(lambda x:x+5)
df2
df2=ds4['col1'].apply(lambda x:x+5)
df2
df2=ds4[['col1','col2']].apply(lambda x:x+5)
df2

#transform()
#it will work same as a apply function
def add_2(x):
    x=x+3
    return x
df1=ds4.transform(add_2)
print(df1)

#map()
#same as a apply and transform
ds4['col1']=ds4['col1'].map(lambda col1:col1/2)
ds4
#using numpy
import numpy as np
ds4['col1']=ds4['col1'].apply(np.square)
ds4
ds4[['col1','col2']]=ds4[['col1','col2']].apply(np.square)
ds4
ds4['col1']=np.square(ds4['col1'])
ds4

########################################################
import pandas as pd
technologies={'courses':['spark','pyspark','hadoop','python','sql','pandas','spark'],
              'Fee':[2000,1200,23400,2400,1455,1256,1500],
              'Duration':['30days','40days','20days','80days','10days','1200days','20days'],
              'Discount':[1000,2300,1200,3400,1200,4500,1200]}
df=pd.DataFrame(technologies)
df
#use groupby to compute the sum
df1=df.groupby(['courses']).sum()
print(df1)
df3=df.groupby(['courses','Duration']).sum()
print(df3)
#reset indexex
df4=df.groupby(['courses','Duration']).sum().reset_index()
print(df4)

###########################################
import pandas as pd
technologies={'courses':['spark','pyspark','hadoop','python','sql','pandas','spark'],
              'Fee':[2000,1200,23400,2400,1455,1256,1500],
              'Duration':['30days','40days','20days','80days','10days','1200days','20days'],
              'Discount':[1000,2300,1200,3400,1200,4500,1200]}
df=pd.DataFrame(technologies)
df
df.columns
col_headers=list(df.columns.values)
print("Column headers",col_headers)

#pandas shuffle dataframe rows
#shuffle the dataframe rows and return all rows
df1=df.sample(frac=1)
print(df1)
df1=df.sample(frac=0.5)
print(df1)
df1=df.sample(frac=0.5).reset_index()
print(df1)
df1=df.sample(frac=1).reset_index(drop=True)  #it drop the shuffle index
print(df1)

#############################################################################
import pandas as pd
technologies1={'course':['spark','pyspark','python','pandas'],
              'fee':[20000,25000,22000,30000],
              'duration':['30days','40days','35days','50days']
              }
labels=['r1','r2','r3','r4']
df1=pd.DataFrame(technologies1,index=labels)
df1

technologies2={'course':['spark','java','python','go'],
              'discount':[2000,2300,1200,2000]
              }
labels=['r1','r6','r3','r5']
df2=pd.DataFrame(technologies2,index=labels)
df2

#------------------------------#joining----------------------------------
#left join- only right cols get match
#right join-only left col get match
#when index dont match the rows get dropped from both dataframes
#left join default joining
#in join we should have one common col 
df3=df1.join(df2,lsuffix="_left",rsuffix="_right")
print(df3)
df3=df1.join(df2,lsuffix="_left",rsuffix="_right",how="inner")
print(df3)
df3=df1.join(df2,lsuffix="_left",rsuffix="_right",how="left")
print(df3)
df3=df1.join(df2,lsuffix="_left",rsuffix="_right",how='right')
print(df3)

df3=df1.set_index('course').join(df2.set_index('course'),how="inner")
print(df3)
df3=df1.set_index('course').join(df2.set_index('course'),how="left")
print(df3)
df3=df1.set_index('course').join(df2.set_index('course'),how="right")
print(df3)

#------------------------------------------------------------------------------
import pandas as pd
df=pd.DataFrame({'course':['spark','pyspark','python','pandas'],
              'fee':[20000,25000,22000,30000],
              
              })
df1=pd.DataFrame({'course':['spark','java','python','go'],
             'fee':[20000,25000,22000,30000]
             })

data=[df,df1]
df2=pd.concat(data)
df2
df2=pd.concat(data).reset_index(drop=True)
df2
#------------------------------------------------------------------------------
#concate multiple dataframe
import pandas as pd
df=pd.DataFrame({'course':['spark','pyspark','python','pandas'],
              'fee':[20000,25000,22000,30000],
              
              })
df1=pd.DataFrame({'course':['spark','java','python','go'],
             'fee':[20000,25000,22000,30000]
             })
df2=pd.DataFrame({'duration':['30days','40days','35days','50days'],
                 'discount':[2000,2300,1200,2000]
                 })

df3=pd.concat([df,df1,df2])
print(df3)






