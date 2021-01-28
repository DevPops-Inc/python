#!/bin/python

# add function

# declare variables 
a = int(input("Let's add in Python!\nType first number:\n "))
b = int(input("Type second number:\n "))

# define add function 
def add(a, b):
    result = a + b
    return result

# print result
print("The result is: ") 
print(add(a, b))
