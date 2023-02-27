#!/bin/python

# count days in month

# you can run this script with: python3 countDaysInMonthInPython.py < year > < month > 

import calendar, colorama, os, sys, time, traceback
from colorama import Fore, Style
from datetime import datetime
colorama.init()


def checkOS():
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
        year = int(input("Please type the year and press the \"Enter\" key (Example: 2020): "))
        print("")

    else: 
        year = int(input("Please type the year and press the \"return\" key (Example: 2020): "))
        print("")

    return year


def getMonth(operatingSystem): 
    if operatingSystem == "Windows": 
        month = int(input("Please type the number of the month and press the \"Enter\" key (Example for March: 3): "))

        print("")

    else: 
        month = int(input("Please type the number of the month and press the \"Enter\" key (Example for March: 3): "))

        print("")

    return month


def checkParameters(year, month): 
    print("Started checking parameter(s) at", datetime.now().strftime("%m-%d-%Y %I:%M %p"))
    valid = True

    print("Parameter(s):")
    print("------------------------")
    print("year : {0}".format(year))
    print("month: {0}".format(month))
    print("------------------------")

    if year == None: 
        print(Fore.RED + "year is not set." + Style.RESET_ALL)
        valid = False

    if month == None: 
        print(Fore.RED + "month is not set." + Style.RESET_ALL)
        valid = False

    if valid == True: 
        print(Fore.GREEN + "All parameter check(s) passed." + Style.RESET_ALL)

        print("Finished checking parameter(s) at", datetime.now().strftime("%m-%d-%Y %I:%M %p"))
        print("")

    else: 
        print(Fore.RED + "One ore more parameters are incorrect." + Style.RESET_ALL)

        print("Finished checking parameter(s) at", datetime.now().strftime("%m-%d-%Y %I:%M %p"))
        exit("")


def countDaysOfMonth(): 
    print("\nLet's count the days in a month in Python!\n")
    operatingSystem = checkOS()

    if len(sys.argv) >= 2: 
        year  = int(sys.argv[1])
        month = int(sys.argv[2])

    else: 
        year  = getYear(operatingSystem)
        month = getMonth(operatingSystem)

    checkParameters(year, month)

    try: 
        startDateTime = datetime.now()
        print("Started counting days in a month at", startDateTime.strftime("%m-%d-%Y %I:%M %p"))

        cal = calendar.TextCalendar(calendar.SUNDAY)
        
        print(Fore.BLUE + "Counting the number of days in {0} {1} now: ".format(calendar.month_name[month], year))

        time.sleep(1)

        for days in cal.itermonthdays(year, month):
            
            if days != 0: 
                time.sleep(0.25)
                print(days)

        print("days in {0} {1}.".format(calendar.month_name[month], year))

        print(Fore.GREEN + "Successfully counted days in a month," + Style.RESET_ALL)

        finishedDateTime = datetime.now()
        print("Finished counting day in a month at", finishedDateTime.strftime("%m-%d-%Y %I:%M %p"))

        duration = finishedDateTime - startDateTime
        print("Total execution time: {0} second(s)".format(duration.seconds))
        print("")

    except Exception: 
        print(Fore.RED + "Failed to count days in a month.")
        
        traceback.print_exc()
        exit("" + Style.RESET_ALL)


countDaysOfMonth()
    