#!/bin/python 

# split string into char in Python 

# you can run this script with: python3 splitStringIntoCharsInPython.py "< string with characters >"

import colorama, os, sys, traceback
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


def getStringWithChars(operatingSystem): 
    if operatingSystem == "Windows": 
        stringWithChars = str(input("Please type a string and press the \"Enter\" key (Example: string): "))

    else: 
        stringWithChars = str(input("Please type a string and press the \"return\" key (Example: string): "))

    print("")
    return stringWithChars


def checkParameters(stringWithChars): 
    print("Started checking parameter(s) at", datetime.now().strftime("%m-%d-%Y %I:%M %p"))
    valid = True 

    print("Parameter(s):")
    print("--------------------------------------------")
    print("stringWithChars: {0}".format(stringWithChars))
    print("--------------------------------------------")

    if stringWithChars == None or stringWithChars == "": 
        print(Fore.RED + "stringWithChars is not set." + Style.RESET_ALL)
        valid = False 

    if valid == True: 
        print(Fore.GREEN + "All parameter check(s) passed." + Style.RESET_ALL)

        print("Finished checking parameter(s) at", datetime.now().strftime("%m-%d-%Y %I:%M %p"))
        print("")

    else: 
        print(Fore.RED + "One or more parameters are incorrect." + Style.RESET_ALL)

        print("Finished checking parameter(s) at", datetime.now().strftime("%m-%d-%Y %I:%M %p"))
        exit("")

    
def splitStringIntoChars(): 
    print("\nSplit string into characters in Python.\n")
    operatingSystem = checkOs()

    if len(sys.argv) >= 2: 
        stringWithChars = str(sys.argv[1])

    else: 
        stringWithChars = getStringWithChars(operatingSystem)

    checkParameters(stringWithChars)

    try: 
        startDateTime = datetime.now()
        
        print("Started splitting string into characters at", startDateTime.strftime("%m-%d-%Y %I:%M %p"))

        splitStringWithChars=list(stringWithChars)
        print(Fore.BLUE, end="")
        print(splitStringWithChars)
        print(Fore.GREEN + "Successfully split string into chars." + Style.RESET_ALL)

        finishedDateTime = datetime.now()
        
        print("Finished splitting string into characters at", finishedDateTime.strftime("%m-%d-%Y %I:%M %p"))

        duration = finishedDateTime - startDateTime
        print("Total execution time: {0} second(s)".format(duration.seconds))
        print("")

    except Exception: 
        print(Fore.RED + "Failed to split string into characters.")
        traceback.print_exc()
        exit("" + Style.RESET_ALL)


splitStringIntoChars()
