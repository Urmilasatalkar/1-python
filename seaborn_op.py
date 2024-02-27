# SEABORN LIBRARY
import seaborn as sns
import pandas
import matplotlib.pyplot as plt
#seaborn has 18 inbuilt datasets
sns.get_dataset_names()
df = sns.load_dataset('titanic')
df.head()

#####################################

#countplot is helpful when dealing with categorial values
sns.countplot(x='sex',data=df)

sns.countplot(x = 'sex',hue ='survived', data = df, palette='Set1')
sns.countplot(x = 'sex',hue ='survived', data = df, palette='Set2')
sns.countplot(x = 'sex',hue ='survived', data = df, palette='Set3')

#***************************************
# there are 3 sets with different color combination palletes
#hue - the name of catagorial col to split the bar
#pallet - the color palette to be used

####################################
#KDE plot
#kernel density estimation plot
#to plot distribution of contineous data

sns.kdeplot(x = 'age',data=df,color='black')

####################################
#distribution plot  --> 
sns.displot(x = 'age',kde = True,bins=6,data=df)
#kde- by default it is false
#bins = no. of bars
#lower the number , wider the bars and wider the interval

######################################
df = sns.load_dataset('iris')
df.head()

sns.jointplot(x = 'sepal_length',y ='petal_length',data=df,kind='reg')
sns.jointplot(x = 'sepal_length',y ='petal_length',data=df,kind='hist')
sns.jointplot(x = 'sepal_length',y ='petal_length',data=df,kind='kde')


sns.pairplot(df)
corr=df.corr()
sns.heatmap(corr)