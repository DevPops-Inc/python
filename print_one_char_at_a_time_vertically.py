#!/bin/python

# print one char at a time vertically

# import module
import time

# declare variable 
string = 'This has been the best week in a long time!'

# define function
def delay_print(string):
    # define for loop
    for char in string: 
        print(char)
        time.sleep(.25)
    
# call function and pass in string
delay_print(string)
