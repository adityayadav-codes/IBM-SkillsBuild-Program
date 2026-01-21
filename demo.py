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
import copy
original = [[1, 2, 3], [4, 5, 6]]
copy.list = copy.deepcopy(original)
copy.list[1][1]= 99
print("Original:", original)
print("copy: ", copy.list)

#  numpy -> numerical python:- library used for numerical computations in python
import numpy as np
a = np.array([1, 2, 3, 4, 5])
print(np.zeros((3)))
print(np.ones((3)))
print(np.arange(1, 11, 3))

