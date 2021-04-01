#!/bin/python

# get local admin password expiration policy on Windows 

# import OS module 
import os

# prompt user input 
str(input("Get local admin password expiration policy on Windows.\nPress any key to continue.\n"))

# get local admin password expiration policy
os.system('net user administrator | findstr /C:expires')
