#!/bin/python

# print one char at a time vertically

# import module
import time

# prompt user input
str(input("\nPrint one char at a time vertically.\nPress any key to continue or press Ctrl and C keys to quit.\n"))

# declare verticalString variable 
verticialString = str(input("\nWhat would you like to print vertically?\n"))

# define function
def delayPrint(verticialString):
    # define for loop
    for char in verticialString: 
        print("\n", char)
        time.sleep(.25)
    
# call function and pass in verticialString
delayPrint(verticialString)
