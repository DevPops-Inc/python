#!/bin/python

# get calendar by year in Python

# you can run this script with: python3 getCalByYearInPython.py < year >

import calendar, colorama, os, sys, traceback
from colorama import Fore, Style
from datetime import datetime
colorama.init()


def checkOs():
    print("Started checking operating system at", datetime.now().strftime("%m-%d-%Y %I:%M %p"))

    if sys.platform == "win32": 
        print(Fore.GREEN + "Operating System:", end=""); sys.stdout.flush()
        os.system('ver')
        print(Style.RESET_ALL, end="")
        operatingSystem = "Windows"

    elif sys.platform == "darwin": 
        print(Fore.GREEN + "Operating System: ")
        os.system('sw_vers')
        print(Style.RESET_ALL, end="")
        operatingSystem = "macOS"

    elif sys.platform == "linux": 
        print(Fore.GREEN + "Operating System: ")
        os.system('uname -r')
        print(Style.RESET_ALL, end="")
        operatingSystem = "Linux"

    print("Finished checking operating system at", datetime.now().strftime("%m-%d-%Y %I:%M %p"))

    print("")
    return operatingSystem


def getYear(operatingSystem): 
    if operatingSystem == "Windows":
        year = int(input("Please type the year you want a calendar for and press \"Enter\" key (Example: 1999): "))
        
    elif operatingSystem == "macOS" or operatingSystem == "Linux": 
        year = int(input("Please type the year you want a calendar for and press \"return\" key (Example: 1999): "))

    print("")
    return year


def checkParameters(year): 
    print("Started checking parameter(s) at", datetime.now().strftime("%m-%d-%Y %I:%M %p"))
    valid = True

    print("Parameter(s):")
    print("----------------------")
    print("year: {0}".format(year))
    print("----------------------")

    if year == None or year == "": 
        print(Fore.RED + "year is not set." + Style.RESET_ALL)
        valid = False

    if valid == True: 
        print(Fore.GREEN + "All parameter check(s) passed." + Style.RESET_ALL)

        print("Finished checking parameter(s) at", datetime.now().strftime("%m-%d-%Y %I:%M %p"))
        print("")

    else: 
        raise Exception("One or more parameters are incorrect.")


def getCalendarByYear(): 
    print("\Let's get a calendar by year in Python!\n")
    operatingSystem = checkOs()

    if len(sys.argv) >= 2: 
        year = int(sys.argv[1])

    else: 
        year = getYear(operatingSystem)

    checkParameters(year)

    try: 
        startDateTime = datetime.now()
        print("Started getting calendar by year at", startDateTime.strftime("%m-%d-%Y %I:%M %p"))

        print("")
        calendar.prcal(year)
        print("")
        
        print(Fore.GREEN + "Successfully got calendar by year" + Style.RESET_ALL)

        finishedDateTime = datetime.now()
        print("Finished getting calendar by year at", finishedDateTime.strftime("%m-%d-%Y %I:%M %p"))

        duration = finishedDateTime - startDateTime
        print("Total execution time: {0} second(s)".format(duration.seconds))
        print("")
        
    except Exception: 
        print(Fore.RED + "Failed to get calendar by year.")
        traceback.print_exc()
        exit("" + Style.RESET_ALL)


getCalendarByYear()
