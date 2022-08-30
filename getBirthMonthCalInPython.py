#!/bin/python

# get birthday month calendar in Python

# you can run this script with: python3 getBirthMonthCalInPython.py < year > < month >

import calendar, colorama, os, sys, traceback
from colorama import Fore, Style
from datetime import datetime
colorama.init()

def checkOs():
    print("Started checking operating system at", datetime.now().strftime("%Y-%m-%d %H:%M %p"))

    if sys.platform == "win32": 
        print(Fore.GREEN + "Operating System: ")
        print(os.system('ver'))
        print(Style.RESET_ALL)
        operatingSystem = "Windows"

    elif sys.platform == "darwin": 
        print(Fore.GREEN + "Operating System: ")
        print(os.system('sw_vers'))
        print(Style.RESET_ALL)
        operatingSystem = "macOS"

    elif sys.platform == "linux": 
        print(Fore.GREEN + "Operating System: ")
        print(os.system('uname -r'))
        print(Style.RESET_ALL)
        operatingSystem = "Linux"

    print("Finished checking operating system at", datetime.now().strftime("%Y-%m-%d %H:%M %p"))

    print("")
    return operatingSystem

def getYear(operatingSystem): 
    if operatingSystem == "Windows":
        year = int(input("Please type the year you want a calendar for and press \"Enter\" key (Example: 1999): "))

        print("")
        
    elif operatingSystem == "macOS" or operatingSystem == "Linux": 
        year = int(input("Please type the year you want a calendar for and press \"return\" key (Example: 1999): "))

        print("")
    
    return year

def getMonth(operatingSystem): 
    if operatingSystem == "Windows":
        month = int(input("Please type the month you want a calendar for and press \"Enter\" key (Example: 12): "))

        print("")
        
    elif operatingSystem == "macOS" or operatingSystem == "Linux": 
        month = int(input("Please type the month you want a calendar for and press \"return\" key (Example: 12): "))

        print("")
    
    return month

def checkParameters(year, month): 
    print("Started checking parameters at", datetime.now().strftime("%Y-%m-%d %H:%M %p"))
    
    valid = "true"

    print("Parameters:")
    print("------------------------")
    print("year : {0}".format(year))
    print("month: {0}".format(month))
    print("------------------------")

    if year == None: 
        print(Fore.RED + "year is not set." + Style.RESET_ALL)
        valid = "false"

    if month == None: 
        print(Fore.RED + "month is not set." + Style.RESET_ALL)
        valid = "false"

    if valid == "true": 
        print(Fore.GREEN + "All parameter checks passed." + Style.RESET_ALL)

        print("Finished checking parameters at", datetime.now().strftime("%y-%m-%d %H:%M %p"))

        print("")

    else: 
        print(Fore.RED + "One or more parameters are incorrect." + Style.RESET_ALL)

        print("Finished checking parameters at", datetime.now().strftime("%y-%m-%d %H:%M %p"))

        exit("")

def getBirthMonthCal(): 
    print("\Let's get birthday month calendar in Python!\n")
    operatingSystem = checkOs()

    if len(sys.argv) >= 2: 
        year  = int(sys.argv[1])
        month = int(sys.argv[2])

    else: 
        year  = getYear(operatingSystem)
        month = getMonth(operatingSystem)

    checkParameters(year, month)

    try: 
        startDateTime = datetime.now()

        print("Started getting birthday month calendar at", startDateTime.strftime("%Y-%m-%d %H:%M %p"))

        print("")
        birthday=calendar.TextCalendar(calendar.SUNDAY)
        birthday.prmonth(year, month)
        print("")
        
        print(Fore.GREEN + "Successfully got birthday month calendar." + Style.RESET_ALL)

        finishedDateTime = datetime.now()

        print("Finished getting birthday month calendar at", finishedDateTime.strftime("%Y-%m-%d %H:%M %p"))

        duration = finishedDateTime - startDateTime
        print("Total execution time: {0} second(s)".format(duration.seconds))
        print("")
        
    except Exception as e: 
        print(Fore.RED + "Failed to get birth month calendar by year.")
        print(e)
        print(traceback.print_stack)
        exit("" + Style.RESET_ALL)

getBirthMonthCal()