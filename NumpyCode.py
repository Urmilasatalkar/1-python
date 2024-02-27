# -*- coding: utf-8 -*-
"""
Created on Thu Aug 10 09:27:42 2023

@author: urmii
"""
#------------------------------------------------------------------------------
#one dimensional array
import numpy as np
arr=np.array([12,23,45,67,89,0])     #[12 23 45 67 89  0]
print(arr)
#-------------------------------------------------------------------------------
#multidimensional array
arr=np.array([[1,2,3],[5,6,7]])    #[[1 2 3]
print(arr)                         #[5 6 7]]
#-------------------------------------------------------------------------------------
#represent the minimum dimesion
#use admin param to specify how many dimensions you want
#to create an array with min dimensions
arr=np.array([12,34,56,78,23],ndmin=2) #[[12,34,45,78,23]]
print(arr)
arr=np.array([12,34,56,78,23],ndmin=5)
print(arr)
#--------------------------------------------------------------------------------
#change the data types
#dtype param
arr=np.array([10,20,30],dtype=complex)          #[10.+0.j 20.+0.j 30.+0.j]
print(arr)
#------------------------------------------------------------------------------
#get the dimension of array
arr=np.array([[1,2,3,4],[4,5,6,7]])
n=arr.ndim
print(n)                    #2
#------------------------------------------------------------------------------------
#finding the size of items in the array
arr=np.array([3,4,5,6,7,8,90])
print("Size of each item:",arr.itemsize)    #4
#-----------------------------------------------------------------------------
#find dtype of array
print("Dtype of each item:",arr.dtype)
#------------------------------------------------------------------------------
#get the shape and size of array
#properties
arr=np.array([[10,20,30,40,50],[60,70,80,90,100]])
print("Size of array:",arr.size)    #10
print("Shape of array:",arr.shape)  #(2,5)
#-----------------------------------------------------------------------------
#create the sequence of integer using arrays
#create sequence if int
#from 0 to 20 with stpes of 3
arr=np.arange(0,20,3)
print("Seq of array:",arr)  # [ 0  3  6  9 12 15 18]
#-----------------------------------------------------------------------------
#access single element using index
arr=np.arange(11)
print(arr)        #[ 0  1  2  3  4  5  6  7  8  9 10]
print(arr[2])       #2
print(arr[-2])     #9
#-----------------------------------------------------------------------------------
#multidimensional array indexing
#access multidimensional array using index
arr=np.array([[10,20,30,40,50,10],[20,30,40,50,60,70]])
print(arr)
print(arr.shape)           #(2,6)
print(arr[1,1])
print(arr[0,4])
print(arr[1,-1])
#---------------------------------------------------------------------------------------
#access element using slicing
arr=np.array([1,2,3,4,5,6,7,8,9,0])
print(arr[1:8:1])       #[2 3 4 5 6 7 8]
print(arr[1:8:2])       #[2 4 6 8]
print(arr[-1:-6:-1])    #[3 2 1 0 9]
print(arr[-2:3:-1])     #[2 1 0 9 8 7 6 5]
print(arr[-5:7])       #[9 0]
#-------------------------------------------------------------------------------
#indexing in numpy
multi_array=np.array([[10,20,30,40],
                      [40,50,60,70],
                      [10,30,40,780],
                      [12,23,45,67]
                      ])
print(multi_array)
multi_array[1,2]   #60
multi_array[1,:]   #array([40,50,60,70])
multi_array[:,1]   #([20,50,30,23])
x=multi_array[:3,::2]        #[[10 30]
                            # [40 60]
                            # [10 40]]
print(x)
x=multi_array[:3,::1]
print(x)
#-----------------------------------------------------------------
#integer array indexing
arr=np.arange(35).reshape(5,7)  #number 0 to 34 5 rows and 7 col
print(arr)
arr=np.arange(42).reshape(6,7)
print(arr)
#------------------------------------------------------------------------------
#boolean array indxing
arr=np.array([[10,20,30,40,50,10],
              [20,30,40,50,60,70],
              [12,23,45,67,23,45],
              ])
row=np.array([False,True,True])   #0th row dont want=False  2nd and 3rd rows want->True
wanted_rows=arr[row,:]    #row already mention and all col
print(wanted_rows)      #[[20 30 40 50 60 70]
                        # [12 23 45 67 23 45]]
#-----------------------------------------------------------------------------------
#convert numpy array into list
array=np.array([10,20,30,40])
print("Array:",array)
print(type(array))      #<class 'numpy.ndarray'>

lst=array.tolist()
print("List:",lst)
print(type(lst))        #<class 'list'>

#-----------------------------------------------------------------------------
#convert multi dimesional array into list
arr=np.array([[10,20,30,40,50,10],
              [20,30,40,50,60,70],
              [12,23,45,67,23,45],
              ])
lst=arr.tolist()
print("Multi Array:",lst)
print(type(lst))       # <class 'list'>
#------------------------------------------------------------------------------
#convert python list into numpy array
#numpy.array()
#numpy.asarray()
list=[1,2,3,4,5,6]
array=np.array(list)
print(type(array))      #<class 'numpy.ndarray'>
array=np.asarray(list)
print(type(array))
#------------------------------------------------------------------------------
#resize the array
#shape manipulation use in NLP
#for voice processing
#fourier transform is used
arr=np.array([[10,20,30,40,50,10],
              [20,30,40,50,60,70],
              [12,23,45,67,23,45],
              ])
arr.shape=[2,9]
arr.shape
arr.size
print(arr)
print(arr)

#reshape()
new_array=arr.reshape(18,1)
print(new_array)

#checking version
import numpy as np
print(np.__version__)


#write a numpy program to test wether
#none of the elements of a given array are zero
x=np.array([1,2,3,4])
print(x)
print(np.all(x))  #True
print("Zero is there or not in array:")
x=np.array([1,2,3,4,0])
print(x)
print("zero is present in array")
print(np.all(x))  #False

#write numpy program are given array are non zero
x=np.array([1,2,3,4])
print(x)
print(np.any(x))  #True
print("Zero is there or not in array:")
x=np.array([0,0,0,0])   
print(x)
print("zero is present in array")
print(np.any(x))  #False

#write numpy program to est a given array
#elemnt wise for finiteness(not infinity or not a number)
import numpy as np
a=np.array([1,0,np.nan,np.inf])
print(a)
print("Test a given array is finiteness or not")
print(np.isfinite(a))

#write numpy program to  test
#element -wise for nan of a given array
a=np.array([1,0,np.nan,np.inf])
print(a)
print(np.isnan(a))

#write a program to create element wise
#comparisionn(geater,greater_q_equal,less and <=)
x=np.array([2,5])
y=np.array([3,5])
print("Greater:")
print(np.greater(x,y))
print("Greater_equal:")
print(np.greater_equal(x,y))
print("Less:")
print(np.less(x,y))
print("Less than:")
print(np.less_equal(x,y))

#write a numpy program to create 3X3 identity matrix
array=np.identity(3)
print("3X3 matrix:")
print(array)

#write a numpy to generate a random number
#between 0 and 1
#numpy.random.normal give the sample random number
rand_num=np.random.normal(0,1,2)  #2 means it give two random number
print(rand_num)
#3x4 array and iterate over it
import numpy as pd
a=np.arange(10,22).reshape((3,4))
print(a)
for x in np.nditer(a):
    print(x,end=' ')
    print()

#write numpy program to create a
#vector of length 5 with values evenly distrubuted
#between 10 and 50
#between 10 to 50 it give 5 random number
v=np.linspace(10,49,5)
#10-starting point
#46-ending point
#5-nos in vector
print(v)

#write a numpy program to create 3x3 matrix
#with values ranging from 2 to 10
x=np.arange(2,11).reshape(3,3)
print(x)

#write numpy program to reverse a array
#first elemet be the last
x=np.arange(12,38)
print(x)
print(x[::-1])
print(x)

#multiplication of two matrices
p=[[1,0],[0,1]]
q=[[1,2],[3,4]]
print(p)
print(q)
result=np.dot(p,q)
print(result)

#write a numpy program to compute
#the cross product of given two matrices
p=[[1,0],[0,1]]
q=[[1,2],[3,4]]
result1=np.cross(p,q)
result2=np.cross(q,p)
print(result1)
print(result2)

#compute the determinant of a given square array
a=np.array([[1,0],[1,2]])
print(a)
print(np.linalg.det(a))

#write anumpy to compute
#the  eigenvalues and right eigenvectors
#of a given square array
m=np.mat("3 -2;1 0")
print(m)
w,v=np.linalg.eig(m)
print("Eigen values of the matrix ",w)
print("Eigen vector of said matrix",v)

#write a numpy program to compute
#the inverse of a given matrix
m=np.array([[1,2],[3,4]])
print(m)
result=np.linalg.inv(m)
print("Reverse matrix:\n",result)







