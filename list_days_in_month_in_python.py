#!/bin/python

# list number of days in a month

# import calendar module 
import calendar

# prompt user input
str(input("\nList number of days in a month.\nPress any key to continue or press Ctrl and C keys to quit.\n"))

# declare year, month and cal variables 
year=int(input("\nWhat is the year? "))
month=int(input("\nWhat is the month number? "))
cal=calendar.TextCalendar(calendar.SUNDAY)

# define for loop and print days
for days in cal.itermonthdays(year, month):
    print(days)
    