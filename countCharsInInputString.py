#!/bin/python

# count characters in input string

# you can run this script with: python3 countCharsInInputString.py '< input string >'

import colorama, os, sys, traceback
from colorama import Fore, Style
from datetime import datetime
colorama.init()


def checkOs(): 
    print("Started checking operating system at", datetime.now().strftime("%m-%d-%Y %I:%M %p"))

    if sys.platform == "win32": 
        print(Fore.GREEN + "Operating System", end=""); sys.stdout.flush()
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


def getInputString(operatingSystem): 
    if operatingSystem == "Windows": 
        inputString = str(input("Please type something you want the character count for and press \"Enter\" key (Example: Python rocks!): "))

    elif operatingSystem == "macOS" or operatingSystem == "Linux": 
        inputString = str(input("Please type something you want the character count for and press \"return\" key (Example: Python rocks!): "))

    print("")
    return inputString


def checkParameters(inputString): 
    print("Started checking parameter(s) at", datetime.now().strftime("%m-%d-%Y %I:%M %p"))
    valid = True

    print("Parameter(s):")
    print("------------------------------------")
    print("inputString: {0}".format(inputString))
    print("------------------------------------")

    if inputString == None or inputString == "": 
        print(Fore.RED + "inputString is not set." + Style.RESET_ALL)
        valid = False

    if valid == True: 
        print(Fore.GREEN + "All parameter check(s) passed." + Style.RESET_ALL)

        print("Finished checking parameter(s) at", datetime.now().strftime("%m-%d-%Y %I:%M %p"))
        print("")

    else: 
        raise Exception("One or more parameters are incorrect.")


def countCharsInInputString(): 
    print("\nLet's count characters in an input string in Python.\n")

    try: 
        operatingSystem = checkOs()

        if len(sys.argv) >= 2: 
            inputString = str(sys.argv[1])

        else: 
            inputString = getInputString(operatingSystem)

        checkParameters(inputString)
        
        startDateTime = datetime.now()
        print("Started counting characters at", startDateTime.strftime("%m-%d-%Y %I:%M %p"))

        print(Fore.BLUE + "The string \"{0}\" has {1} characters.".format(inputString, len(inputString)))

        print(Fore.GREEN + "Successfully counted characters in input string." + Style.RESET_ALL)

        finishedDateTime = datetime.now()
        print("Finished counting characters at", finishedDateTime.strftime("%m-%d-%Y %I:%M %p"))

        duration = finishedDateTime - startDateTime
        print("Total execution time: {0} second(s)".format(duration.seconds))
        print("")
        
    except Exception: 
        print(Fore.RED + "Failed to count characters in string.")
        traceback.print_exc()
        exit("" + Style.RESET_ALL)


countCharsInInputString()
