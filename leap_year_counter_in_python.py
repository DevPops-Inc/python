#!/bin/python

# display number of leap years between two years

# import calendar module
import calendar

print("Number of Leap Years Between Two Years\n")

# declare variables 
year1=int(input("Enter the first year: "))
year2=int(input("Enter the sceond year: "))
leap=calendar.leapdays(year1, year2)

print("Number of leap years between", year1, "and", year2, "is", leap)