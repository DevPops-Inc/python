#!/bin/python 

# check disk and restart Windows

# import OS module 
import os

# check disk
os.system('echo y | chkdsk /f/r c:')

# print message to user and wait for user input
str(input("Please save your documents and close applications. Press any key to restart Window."))

# restart Windows 
os.system('shutdown /r /t 0')
