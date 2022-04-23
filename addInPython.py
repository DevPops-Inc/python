#!/bin/python

# add in Python

# you can run this script with: python3 add_function.py < first number > < second number >

import colorama, os, sys, traceback
from colorama import Fore, Style 
from datetime import datetime
colorama.init()

def checkOs():
    print("Started checking operating system at ", datetime.now().strftime("%Y-%m-%d %H:%M %p"))

    if sys.platform == "Windows":
        print(Fore.GREEN + "Operating System: Windows" + Style.RESET_ALL)
        operatingSystem = "Windows"
    elif sys.platform == "darwin": 
        print(Fore.GREEN + "Operating System: ")
        print(os.system('sw_vers'))
        print(Style.RESET_ALL)
        operatingSystem = "macOS"
    else: 
        print(Fore.GREEN + "Operating System: Linux" + Style.RESET_ALL)
        operatingSystem = "Linux"
    
    print("Finished checking operating system at ", datetime.now().strftime("%Y-%m-%d %H:%M %p"))

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
    print("Started checking parameters at", datetime.now().strftime("%Y-%m-%d %H:%M %p"))

    valid = "true"

    print("Parameters:")
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
        print(Fore.GREEN + "All parameter checks passed." + Style.RESET_ALL)

        print("Finished checking parameters at", datetime.now().strftime("%Y-%m-%d %H:%M %p"))
        print("")
    else:
        print(Fore.RED + "One or more parameter checks are incorrect." + Style.RESET_ALL)

        print("Finished checking parameters at", datetime.now().strftime("%Y-%m-%d %H:%M %p"))
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
        start=datetime.now()
        print("Started adding at", start.strftime("%Y-%m-%d %H:%M %p"))
        
        result = firstNumber + secondNumber
        
        print(Fore.YELLOW + "{0} + {1} = {2}".format(firstNumber, secondNumber, result))
        
        print(Fore.GREEN + "Successfully added in Python" + Style.RESET_ALL)

        finished = datetime.now()
        print("Finished adding at", finished.strftime("%Y-%m-%d %H:%M %p"))
        
        duration = finished - start
        print("Total execution time: {0} second(s)".format(duration.seconds))
        print("")
    except Exception as e: 
        print(Fore.RED + "Failed to add in Python.")
        print(e)
        print(traceback.print_stack)
        exit("" + Style.RESET_ALL)
        
addFunction()
