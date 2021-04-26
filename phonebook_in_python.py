#!/bin/python

# phonebook

# prompt user input 
str(input("\nPhonebook.\nPress any key to continue or press Ctrl and C keys to quit.\n")

# create blank dictionary
phonebook={}

# define user inputs
name=input("\nEnter name: ")
number=int(input("\nEnter phone number: "))

# add user's inputted variables to blank dictionary
phonebook[name] = number

# print dictionary
print(phonebook)
