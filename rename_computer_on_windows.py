#!/bin/python

# rename computer on Windows

# import OS module 
import os

# prompt user input
str(input("Rename computer on Windows.\nPress any key to continue or press Ctrl and C keys to quit.\n"))

# get current computer name
print("Your computer's current name is: \n")
os.system('hostname')

# declare variables
oldName = str(input("Please type your computer's current name here: \n"))
newName = str(input("What would you like the name new to be?\n"))
renameComputer = "WMIC computersystem where caption={0} rename {1}".format(oldName, newName)

# rename computer and show new name
os.system(renameComputer)
print("Your computer's current name is: \n")
os.system('hostname')
