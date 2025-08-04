#!/bin/python

# find the greatest common divisor of two numbers with Euclid's algorithm in Python

# you can run this script with euclidsAlgorithmInPython.py < first number > < second number > 

import colorama, os, sys, traceback
from colorama import Fore, Style 
from datetime import datetime
colorama.init()


def checkOs(): 
    print("Started checking operating system at", datetime.now().strftime("%m-%d-%Y %H:%M %p"))

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
        print(Fore.GREEN + "Operating System")
        os.system('uname -r')
        print(Style.RESET_ALL, end="")
        operatingSystem = "Linux"

    print("Finished checking operating system at", datetime.now().strftime("%m-%d-%Y %H:%M %p"))

    print("")
    return operatingSystem


def getFirstNumber(operatingSystem): 
    if operatingSystem == "Windows": 
        firstNumber = int(input("Please type the first number and press the \"Enter\" key (Example: 60): "))

    else: 
        firstNumber = int(input("Please type the first number and press the \"return\" key (Example: 60): "))

    print("")
    return firstNumber


def getSecondNumber(operatingSystem): 
    if operatingSystem == "Windows": 
        secondNumber = int(input("Please type the second number and press the \"Enter\" key (Example: 96): "))

    else: 
        secondNumber = int(input("Please type the second number and press the \"Enter\" key (Example: 96): "))

    print("")
    return secondNumber


def checkParameters(firstNumber, secondNumber): 
    print("Started checking parameter(s) at", datetime.now().strftime("%m-%d-%Y %I:%M %p"))
    valid = True

    print("Parameter(s):")
    print("--------------------------------------")
    print("firstNumber : {0}".format(firstNumber))
    print("secondNumber: {0}".format(secondNumber))
    print("--------------------------------------")

    if firstNumber == None or firstNumber == "": 
        print(Fore.RED + "firstNumber is not set." + Style.RESET_ALL)
        valid = False

    if secondNumber == None or secondNumber == "": 
        print(Fore.RED + "secondNumber is not set." + Style.RESET_ALL)
        valid = False

    if valid == True: 
        print(Fore.GREEN + "All parameter check(s) passed." + Style.RESET_ALL)

        print("Finished checking parameter(s) at", datetime.now().strftime("%m-%d-%Y %I:%M %p"))
        print("")

    else: 
        raise Exception("One or more parameters are incorrect.")


def greatestCommonDivisor(firstNumber, secondNumber):
    while (secondNumber != 0):
        t = firstNumber
        firstNumber = secondNumber
        secondNumber = t % secondNumber

    return firstNumber


def euclidsAlgo():
    print("\nFind the greatest common divisor of two numbers with Euclid's Algorithm in Python.\n")

    try: 
        operatingSystem = checkOs()

        if len(sys.argv) >= 2: 
            firstNumber  = int(sys.argv[1])
            secondNumber = int(sys.argv[2])

        else: 
            firstNumber  = getFirstNumber(operatingSystem)
            secondNumber = getSecondNumber(operatingSystem)

        checkParameters(firstNumber, secondNumber)
        
        startDateTime = datetime.now()
        print("Started finding greatest common divisor at", startDateTime.strftime("%m-%d-%Y %I:%M %p"))

        lowestCommonDenomiator = greatestCommonDivisor(firstNumber, secondNumber)
        
        print(Fore.BLUE + "{0} is the greatest common divisor of {1} and {2}.".format(lowestCommonDenomiator, firstNumber, secondNumber))

        print(Fore.GREEN + "Successfully found the greatest common divisor." + Style.RESET_ALL)

        finishedDateTime = datetime.now()

        print("Finished finding greatest common divisor at", finishedDateTime.strftime("%m-%d-%Y %I:%M %p"))

        duration = finishedDateTime - startDateTime
        print("Total execution time: {0} second(s)".format(duration.seconds))
        print("")

    except Exception: 
        print(Fore.RED + "Failed to find greatest common divisor.")
        traceback.print_exc()
        exit("" + Style.RESET_ALL)


euclidsAlgo()
