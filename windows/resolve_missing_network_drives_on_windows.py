#!/bin/python

# resolve missing network drives on Windows 

# import OS module 
import os 

# prompt user input
str(input("Resolve missing network drives on Windows.\nPress any key to continue or press Ctrl and C keys to quit.\n"))

# fix network drives and prompt restart
os.system('GPUpdate /target:user /force')
str.(input("Please save your documents and close applications.\nPress any key to restart computer.\n"))
os.system('shutdown /r /t 0')
