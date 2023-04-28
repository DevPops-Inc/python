#!/bin/python

# leap year counter

# you can run this script with: python3 countLeapYearsInPython.py < first year > < second year >

import calendar, colorama, os, sys, traceback
from colorama import Fore, Style
from datetime import datetime
colorama.init()


def checkOs(): 
    print("Started checking operating system at", datetime.now().strftime("%Y-%d-%m %H:%M %p"))

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

    print("Finished checking operating system at", datetime.now().strftime("%Y-%d-%m %H:%M %p"))
    print("")
    return operatingSystem


def getFirstYear(operatingSystem): 
    if operatingSystem == "Windows": 
        firstYear = int(input("Please type the first year and press the \"Enter\" key (Example: 1981): "))

    else: 
        firstYear = int(input("Please type the first year and press the \"return\" key (Example: 1981): "))
    
    print("")
    return firstYear


def getSecondYear(operatingSystem): 
    if operatingSystem == "Windows": 
        secondYear = int(input("Please type the second year and press the \"Enter\" key (Example: 2023): "))

    else: 
        secondYear = int(input("Please type the second year and press the \"return\" key (Example: 2023): "))

    print("")
    return secondYear


def checkParameters(firstYear, secondYear): 
    print("Started checking parameter(s) at", datetime.now().strftime("%m-%d-%Y %I:%M %p"))
    valid = True

    print("Parameter(s): ")
    print("----------------------------------")
    print("firstYear : {0}".format(firstYear))
    print("secondYear: {0}".format(secondYear))
    print("----------------------------------")

    if firstYear == None or firstYear == "": 
        print(Fore.RED + "firsYear is not set." + Style.RESET_ALL)
        valid = False

    if secondYear == None or secondYear == "": 
        print(Fore.RED + "secondYear is not set." + Style.RESET_ALL)
        valid = False

    if valid == True: 
        print(Fore.GREEN + "All parameter check(s) passed." + Style.RESET_ALL)

        print("Finished checking parameter(s) at", datetime.now().strftime("%m-%d-%Y %I:%M %p"))
        print("")

    else: 
        print(Fore.RED + "One or more parameters are incorrect." + Style.RESET_ALL)

        print("Finished checking parameter(s) at", datetime.now().strftime("Y-%m-%d %H:%M %p"))
        exit("")

        
def leapYearCounter(): 
    print("\nLet's count number of leap years between two years in Python!\n")
    operatingSystem = checkOs()

    if len(sys.argv) >= 2: 
        firstYear  = int(sys.argv[1])
        secondYear = int(sys.argv[2])

    else: 
        firstYear  = getFirstYear(operatingSystem)
        secondYear = getSecondYear(operatingSystem)

    checkParameters(firstYear, secondYear)

    try: 
        startDateTime = datetime.now()
        print("Started counting leap years at", startDateTime.strftime("%m-%d-%Y %I:%M %p"))

        leapYears = calendar.leapdays(firstYear, secondYear)
        
        print(Fore.BLUE + "There are {0} leap years between {1} and {2}.".format(leapYears, firstYear, secondYear))

        print(Fore.GREEN + "Successfully counted number of leap years." + Style.RESET_ALL)

        finishedDateTime = datetime.now()
        print("Finished counting leap years at", finishedDateTime.strftime("%m-%d-%Y %I:%M %p"))

        duration = finishedDateTime - startDateTime
        print("Total execution time: {0} second(s)".format(duration.seconds))
        print("")

    except Exception: 
        print(Fore.RED + "Failed to count leap years.")
        traceback.print_exc()
        exit("" + Style.RESET_ALL)


leapYearCounter()
