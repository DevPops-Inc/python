#!/bin/python

# leap year counter

# import calendar module
import calendar

# prompt user input 
str(input("\nNumber of Leap Years Between Two Years\nPress any key to continue or press Ctrl and C keys to quit.\n"))

# declare variables 
year1=int(input("\nEnter the first year: "))
year2=int(input("\nEnter the sceond year: "))
leap=calendar.leapdays(year1, year2)

# print number of leap years
print("\nNumber of leap years between", year1, "and", year2, "is", leap)
