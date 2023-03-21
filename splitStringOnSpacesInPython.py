#!/bin/python

# split string on spaces in Python

# you can run this script with: python3 splitStringOnSpacesInPython.py "< string with spaces >"

import colorama, os, sys, traceback 
from colorama import Fore, Style 
from datetime import datetime 
colorama.init()


def checkOs(): 
    print("Started checking operating system at", datetime.now().strftime("%m-%d-%Y %I:%M %p"))

    if sys.platform == "win32": 
        print(Fore.GREEN + "Operating System:", end=""); sys.stdout.flush()
        os.system('ver')
        print(Style.RESET, end="")
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


def getStringWithSpaces(operatingSystem): 
    if sys.platform == "Windows": 
        stringWithSpaces = str(input("Please type a string with spaces and press the \"Enter\" key (Example: string with spaces): "))

    else: 
        stringWithSpaces = str(input("Please type a string with spaces and press the \"return\" key (Example: string with spaces): "))

    print("")
    return stringWithSpaces


def checkParameters(stringWithSpaces): 
    print("Started checking parameter(s) at", datetime.now().strftime("%m-%d-%Y %I:%M %p"))
    valid = True 

    print("Parameter(s):")
    print("----------------------------------------------")
    print("stringWithSpaces: {0}".format(stringWithSpaces))
    print("----------------------------------------------")

    if stringWithSpaces == None: 
        print(Fore.RED + "stringWithSpaces is not set." + Style.RESET_ALL)
        valid = False 

    if valid == True: 
        print(Fore.GREEN + "All parameter check(s) passsed." + Style.RESET_ALL)

        print("Finished checking parameter(s) at", datetime.now().strftime("%m-%d-%Y %I:%M %p"))
        print("")

    else: 
        print(Fore.RED + "One or more parameters are incorrect." + Style.RESET_ALL)

        print("Finished checking parameter(s) at", datetime.now().strftime("%m-%d-%Y %I:%M %p"))
        exit("")


def splitStringOnSpaces(): 
    print("\nSplit string on spaces in Python.\n")
    operatingSystem = checkOs()

    if len(sys.argv) >= 2: 
        stringWithSpaces = str(sys.argv[1])

    else: 
        stringWithSpaces = getStringWithSpaces(operatingSystem)

    checkParameters(stringWithSpaces)

    try: 
        startDateTime = datetime.now()
        
        print("Started splitting string on spaces at", startDateTime.strftime("%m-%d-%Y %I:%M %p"))

        splitStringOnSpaces=stringWithSpaces.split(" ")
        print(Fore.BLUE, end="")
        print(splitStringOnSpaces)
        print(Fore.GREEN + "Successfully split string on spaces." + Style.RESET_ALL)

        finishedDateTime = datetime.now()

        print("Finished splitting string on spaces at", finishedDateTime.strftime("%m-%d-%Y %I:%M %p"))

        duration = finishedDateTime - startDateTime
        print("Total execution time: {0} second(s)".format(duration.seconds))
        print("")

    except Exception: 
        print(Fore.RED + "Failed to split string on spaces.")
        traceback.print_exc()
        exit("" + Style.RESET_ALL)


splitStringOnSpaces()
