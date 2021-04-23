#!/bin/python

# launch YouTube in Chrome on Windows 

# import OS module 
import os

# prompt user response
str(input("\nLaunch YouTube in Chrome on Windows.\nPress any key to continue or press Ctrl and C keys to quit.\n"))

# launch YouTube in Chrome
os.system('start chrome "http://youtube.com"')
