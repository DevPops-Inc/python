#!/bin/python 

# check disk and restart Windows

# import OS module 
import os

# prompt user input
str(input("Check disk and restart Windows.\nPress any key to continue or press Ctrl and C keys to quit.\n"))

# check disk
os.system('echo y | chkdsk /f/r c:')

# print message to user and wait for user input
str(input("Please save your documents and close applications.\nPress any key to restart Windows.\n"))

# restart Windows 
os.system('shutdown /r /t 0')
