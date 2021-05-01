#!/bin/python

# print char at a time

# import time and sys modules 
import time, sys

# prompt user input
str(input("\nPrint char at a time.\nPress any key to continue or press Ctrl and C keys to quit.\n"))

# declare inputString variable 
inputString = str(input("What would you like to print one char at a time?\n"))

# define function
def delayPrint(inputString):
    for char in inputString: 
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.25)

# call function and pass in inputString
delayPrint(inputString)
