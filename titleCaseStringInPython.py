#!/bin/python

# title case your title

# you can run this script with: python3 titleCaseStringInPython.py '< title string >'

import colorama, os, sys, traceback
from colorama import Fore, Style 
from datetime import datetime 
colorama.init()


def checkOs(): 
    print("Started checking operating system at", datetime.now().strftime("%m-%d-%Y %I:%M %p"))

    if sys.platform == "win32": 
        print(Fore.GREEN + "Operating System:", end="")
        os.system('ver')
        print(Style.RESET_ALL, end="")
        operatingSystem = "Windows"

    elif sys.platform == "darwin": 
        print(Fore.GREEN + "Operating System:")
        os.system('sw_vers')
        print(Style.RESET_ALL, end="")
        operatingSystem = "macOS"

    elif sys.platform == "linux":
        print(Fore.GREEN + "Operating System:")
        os.system('uname -r')
        print(Style.RESET_ALL, end="")
        operatingSystem = "Linux"

    print("Finished checking operating system at", datetime.now().strftime("%m-%d-%Y %I:%M %p"))
    print("")
    return operatingSystem


def getTitleString(operatingSystem): 
    if operatingSystem == "Windows": 
        titleString = str(input("Please type the string you wish to title case and press the \"Enter\" key (Example: python rocks!): "))

    else: 
        titleString = str(input("Please type the string you wish to title case and press the \"return\" key (Example: python rocks!): "))

    print("")
    return titleString


def checkParameters(titleString): 
    print("Started checking parameter(s) at", datetime.now().strftime("%m-%d-%Y %I:%M %p"))
    valid = "true"

    print("Parameter(s):")
    print("------------------------------------")
    print("titleString: {0}".format(titleString))
    print("------------------------------------")

    if valid == "true": 
        print(Fore.GREEN + "All parameter check(s) passed." + Style.RESET_ALL)

        print("Finished checking parameter(s) at", datetime.now().strftime("%m-%d-%Y %I:%M %p"))
        print("")

    else: 
        print(Fore.RED + "One or more parameter checks passed." + Style.RESET_ALL)

        print("Finished checking parameter(s) at", datetime.now().strftime("%m-%d-%Y %I:%M %p"))
        exit("")


def titleCaseString(): 
    print("\nTitle case string in Python.\n")
    operatingSystem = checkOs()

    if len(sys.argv) >= 2: 
        titleString = str(sys.argv[1])

    else: 
        titleString = getTitleString(operatingSystem)

    checkParameters(titleString) 

    try: 
        startDateTime = datetime.now()
        
        print("Started title casing \"{0}\" at {1}".format(titleString, startDateTime.strftime("%m-%d-%Y %I:%M %p")))

        print(Fore.BLUE + "\"{0}\" is now \"{1}\"".format(titleString, titleString.title()))

        print(Fore.GREEN + "Successfully title cased \"{0}\"".format(titleString.title()) + Style.RESET_ALL)

        finishedDateTime = datetime.now()

        print("Finished title casing \"{0}\" at {1}".format(titleString.title(), finishedDateTime.strftime("%m-%d-%Y %I:%M %p")))

        duration = finishedDateTime - startDateTime
        print("Total execution time: {0} second(s)".format(duration.seconds))
        print("")

    except Exception as e: 
        print(Fore.RED + "Failed to title case \"{0}\"".format(titleString))
        print(e)
        print(traceback.print_stack)
        exit("" + Style.RESET_ALL)


titleCaseString()
