#!/bin/python

# get local admin password expiration policy on Windows 

# import OS module 
import os

# prompt user input 
str(input("\nGet local admin password expiration policy on Windows.\nPress any key to continue or press Ctrl and C keys to exit.\n"))

# get local admin password expiration policy
os.system('net user administrator | findstr /C:expires')
