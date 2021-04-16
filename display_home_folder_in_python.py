#!/bin/python

# display home folder

# import OS module
import os

# prompt user for input
str(input("\nDisplay home folder.\nPress any key to continue or press Ctrl and C keys to quit.\n"))

# display home folder Python is running on
home=os.getcwd()
print("Your home folder is:", home, "\n")
