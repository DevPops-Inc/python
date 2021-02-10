#!/bin/python

# phonebook

# create blank dictionary
phonebook={}

# define user inputs
name=input("Enter name: ")
number=int(input("Enter phone number: "))

# add user's inputted variables to blank dictionary
phonebook[name] = number

# print dictionary
print(phonebook)
