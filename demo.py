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
from os import sep


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

import copy

a = [[1, 2], [3, 4]]
b = copy.copy(a)

b[1][0] = 99
print(a)  # [[1, 2], [3, 4]]
print(b)  # [[1, 2], [99, 4]]

