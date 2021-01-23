#!/bin/python

# print char at a time

# import modules 
import time
import sys

# declare variable 
string = "This has been best week in a long time!\n"

# define function
def delay_print(string):
    for char in string: 
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.25)

# call function and pass in string
delay_print(string)
