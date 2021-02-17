#!/bin/python

# list number of days in a month

# import calendar module 
import calendar

# declare variables 
year=int(input("What is the year? "))
month=int(input("What is the month number? "))

cal=calendar.TextCalendar(calendar.SUNDAY)
for i in cal.itermonthdays(year, month):
    print(i)
    