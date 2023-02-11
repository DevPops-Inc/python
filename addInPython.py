#!/bin/python

# add in Python

# you can run this script with: python3 addInPython.py < first number > < second number >

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

    
def getFirstNumber(operatingSystem):
    if operatingSystem == "Windows":
        firstNumber = int(input("Type first number and press \"Enter\" key (Example: 2): "))

        print("")

    elif operatingSystem == "macOS" or operatingSystem == "Linux": 
        firstNumber = int(input("Type first number and press \"return\" key (Example: 2): "))

        print("")

    return firstNumber


def getSecondNumber(operatingSystem):
    if operatingSystem == "Windows":
        secondNumber = int(input("Type second number and press \"Enter\" key (Example: 2): "))

        print("")

    elif operatingSystem == "macOS" or operatingSystem == "Linux": 
        secondNumber = int(input("Type second number and press \"return\" key (Example: 2): "))

        print("")

    return secondNumber


def checkParameters(firstNumber, secondNumber):
    print("Started checking parameter(s) at", datetime.now().strftime("%m-%d-%Y %I:%M %p"))

    valid = "true"

    print("Parameter(s):")
    print("---------------------------------------")
    print("firstNumber : {0}".format(firstNumber))
    print("secondNumber: {0}".format(secondNumber))
    print("---------------------------------------")

    if firstNumber == None:
        print(Fore.RED + "firstNumber is not set." + Style.RESET_ALL)
        valid = "false"

    if secondNumber == None:
        print(Fore.RED + "secondNumber is not set." + Style.RESET_ALL)
        valid = "false"

    if valid == "true":
        print(Fore.GREEN + "All parameter check(s) passed." + Style.RESET_ALL)

        print("Finished checking parameter(s) at", datetime.now().strftime("%m-%d-%Y %I:%M %p"))
        print("")

    else:
        print(Fore.RED + "One or more parameter checks are incorrect." + Style.RESET_ALL)

        print("Finished checking parameter(s) at", datetime.now().strftime("%m-%d-%Y %I:%M %p"))

        exit("")        


def addFunction():
    print("\nLet's add in Python!\n")
    operatingSystem = checkOs()

    if len(sys.argv) > 2: 
        firstNumber  = int(sys.argv[1]) 
        secondNumber = int(sys.argv[2])
        
    else: 
        firstNumber  = getFirstNumber(operatingSystem)
        secondNumber = getSecondNumber(operatingSystem)
        
    checkParameters(firstNumber, secondNumber)

    try: 
        startDateTime = datetime.now()
        print("Started adding at", startDateTime.strftime("%m-%d-%Y %I:%M %p"))
        
        result = firstNumber + secondNumber
        
        print(Fore.BLUE + "{0} + {1} = {2}".format(firstNumber, secondNumber, result))
        
        print(Fore.GREEN + "Successfully added in Python" + Style.RESET_ALL)

        finishedDateTime = datetime.now()
        print("Finished adding at", finishedDateTime.strftime("%m-%d-%Y %I:%M %p"))
        
        duration = finishedDateTime - startDateTime
        print("Total execution time: {0} second(s)".format(duration.seconds))
        print("")

    except Exception: 
        print(Fore.RED + "Failed to add in Python.")        
        traceback.print_exc()
        exit("" + Style.RESET_ALL)
        
        
addFunction()
