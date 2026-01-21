# file = open("example.txt", "w")
# file.write("This is a file handling example.")
# file.close()
# file = open("example.txt", "r")
# content = file.read()
# print(content)
# file.close()
# name =input("Enter your name: ")
# print(f"You entered: {name}")
#input -> data given to the program by the user
#output data -> data given by the program to the user
# from os import sep


# a=int(input("Enter a number: "))
# b=int(input("Enter another number: "))
# print(f"The sum of {a} and {b} is {a+b}")
# n = 9

# b = str(a)
# print()
# print(type(b))
# print("hello", "world", sep=" ", end = "!")
# in copy we create as new object instead of sharing memory
# x = [10]
# y = x
# y.append(4)
# print(x)
# print(y)
# x = 10
# y = 20
# print(x)
# print(y)

# import copy

# a = [[1, 2], [3, 4]]
# b = copy.copy(a)

# b[1][0] = 99
# print(a)  # [[1, 2], [3, 4]]
# print(b)  # [[1, 2], [99, 4]]

# # shallow copy
# original = [[1, 2, 3], [4]]
# copy.list = original.copy()
# copy.list[1] = "Aditya "
# copy.list.append("Anil")
# copy.list[0][0] = 99
# print("Original:", original)    
# print("Copy:", copy.list)

# deep copy
# import copy
# original = [1, 2, 3, 4, 5]
# copy.list = copy.deepcopy(original)
# copy.list[1]= 101
# print("original", original)
# print("deep copy", copy.list)


# # shallow copy practice
# import copy
# original = [[1, 2, 3], [4, 5, 6]]
# copy.list = copy.copy(original)
# copy.list[1][1]= 99
# print("Original:", original)
# print("copy: ", copy.list)

# import copy
# original = [[1,2,3,4], [5,6,7]]
# copy.list = copy.copy(original)
# copy.list[0][0] = 99
# print("Original : ", original)
# print("Shallow copy: " , copy.list)

# deep copy practice
# import copy
# original = [[1, 2, 3], [4, 5, 6]]
# copy.list = copy.deepcopy(original)
# copy.list[1][1]= 99
# print("Original:", original)
# print("copy: ", copy.list)

#  numpy -> numerical python:- library used for numerical computations in python
# import numpy as np
# a = np.array([1, 2, 3, 4, 5])
# print(np.zeros((3)))
# print(np.ones((3)))
# print(np.arange(1, 11, 3))
# import numpy as np
#a =  np.array([[1, 2, 3, 4, 5], [2,4,6,8,10]])
#print(a)
#print(a.dtype)
#print(a.shape)
#print(a.size)
#print(a.ndim)
#print(a.transpose())
#print(a.nbytes)
# arr=np.array([1,2,3,4,5,6])
# arr2=arr.reshape(2,3)
#convert 1D array to 2D array
#arr3=arr.reshape(1,2,3)
# print(arr2)
# print(arr3)
# print(arr3.shape)
# a=np.array([1,2,3])
# b=np.array([4,5,6])
# np.concatenate((a,b))
# np.vstack((a,b))
# np.hstack((a,b))
# print(np.concatenate((a,b)))
# print(np.vstack((a,b)))
# print(np.hstack((a,b)))
# arr=np.array([10,20,30,40])
# np.split(arr,2)
# print(arr)
# print(np.where(arr==10))
# print(np.split(arr,2))
#search
# np.where(arr==30)
# np.where(arr>>30)
# print(np.split(arr==2))
# print(np.where(arr>>30))
#sorting
# np.sort(arr)
# print(np.sort(arr))
#filtering
# arr>20
# print(arr>20)
# arr[arr>20]
# print(arr[arr>20])
# #broadcasting
# arr+10
# print(arr+10)
# #Matrix Broadcasting
# matrix=np.array([[10,30,40],[20,10,10]])
# matrix+np.array([10,10,20])

#  Pandas -> library used for data analysis and manipulation in python
import pandas as pd
# s = pd.Series([10, 20, 30, 40, 50])
# print(s)
s = pd.Series([10, 20, 30, 40, 50], index=['a', 'b', 'c', 'd', 'e'])
print(s)
s.name="Column name"
s.index.name="Index name"
print(s)
k=pd.DataFrame(s)
print(k)
data={'Name': ['Alice', 'Bob', 'Charlie', 'David'],
      'Age': [25, 30, 35, 40],
      'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']}
df = pd.DataFrame(data)

# print(df)
# print(df['Name'])
# print(df[['Name', 'Age']])
# print(df.iloc[0])
# print(df.iloc[1:3])
# print(df[df['Age'] > 30])
# df['Age'] = df['Age'] + 1
# print(df)
# df['Country'] = 'USA'
# print(df)  
# df.dtypes
# print(df.dtypes)
# df.shape
# print(df.shape)
# df.columns
# print(df.columns)
# df[["Name","City"]]
# print(df[["Name","City"]])
iloc=df.iloc[2]
print(iloc)
loc=df.loc[2, ["Name", "Age"]]
print(loc)
age=df[df['Age']>30]
print(age)
pd.read_excel("Raw_data.xlsx")