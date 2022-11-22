#!/bin/python

# Windows quick fix

# import OS module 
import os

# prompt user input
str(input("Windows quick fix.\nPress any continue or press Ctrl and C keys to quit.\n"))

# check C:\ drive
os.system('echo y | chkdsk /f c:')

# prompt user to save documents before restart
str(input("Please save your documents and close applications.\nPress any key to continue.\n"))
os.system('shutdown /r /t 0')
