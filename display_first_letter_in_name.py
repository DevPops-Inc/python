#!/bin/python

# display first letter in name 

# call user input with curly brackets 
name=input("What's your name? ")
print("Hello, {}.".format(name))

#  display the first letter in entered name 
lname=list(name)
print("The first letter of your name is a {0}".format(*lname))
