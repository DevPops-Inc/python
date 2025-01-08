#!/bin/python

# capitalize first word in string in Python

# you can run this script with: python3 capsFirstWordInStringInPython.py "< string >"

import colorama, os, sys, traceback
from colorama import Fore, Style 
from datetime import datetime
colorama.init()


def checkOs(): 
    print("Started checking operating system at", datetime.now().strftime("%m-%d-%Y %I:%M %p"))

    if sys.platform == "win32": 
        print(Fore.GREEN + "Operating System:", end=""); sys.stdout.flush()
        print(os.system('vers'))
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


def getTitleString(operatingSystem):
    if operatingSystem == "Windows": 
        titleString = str(input("Please type the string you would like to capitalize the first word of and press \"Enter\" key (Example: python rocks!): "))
    
    elif operatingSystem == "macOS" or operatingSystem == "Linux":
        titleString = str(input("Please type the string you would like to capitalize the first word of and press \"return\" key (Example: python rocks!): "))

    print("")
    return titleString


def checkParameters(titleString):
    print("Started checking parameter(s) at", datetime.now().strftime("%m-%d-%Y %I:%M %p"))
    valid = True

    print("Parameter(s):")
    print("------------------------------------")
    print("titleString: {0}".format(titleString))
    print("------------------------------------")

    if titleString == None or titleString == "": 
        print(Fore.RED + "titleString is not set." + Style.RESET_ALL)
        valid = False

    if valid == True: 
        print(Fore.GREEN + "All parameter check(s) passed." + Style.RESET_ALL)

        print("Finished checking parameter(s) at", datetime.now().strftime("%m-%d-%Y %I:%M %p"))
        print("")

    else: 
        raise Exception("One or more parameters are incorrect.")


def capsFirstWordInString():
    print("\nLet's capitalize the first word in a string in Python!\n")
    operatingSystem = checkOs()

    if len(sys.argv) >= 2: 
        titleString = str(sys.argv[1])
        
    else: 
        titleString = getTitleString(operatingSystem)

    try: 
        checkParameters(titleString)
        
        startDateTime = datetime.now()
        
        print("Started capitalizing first word in string at", startDateTime.strftime("%m-%d-%Y %I:%M %p"))

        capitalizedFirstWord = titleString.capitalize()
        print(Fore.BLUE + capitalizedFirstWord + Style.RESET_ALL)
        print(Fore.GREEN + "Successfully capitalized first word in string." + Style.RESET_ALL)

        finishedDateTime = datetime.now()

        print("Finished capitalizing first word in string at", datetime.now().strftime("%m-%d-%Y %I:%M %p"))

        duration = finishedDateTime - startDateTime
        print("Total execution time: {0} second(s)".format(duration.seconds))
        print("")

    except Exception as e:
        print(Fore.RED + "Failed to capitalize first word in string.")
        traceback.print_exc()
        exit("" + Style.RESET_ALL)


capsFirstWordInString()
