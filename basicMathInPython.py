#!/bin/python

# basic math in Python

import colorama, os, sys, traceback
from colorama import Fore, Style
from datetime import datetime
colorama.init()


def checkOs():
    print("Started checking operating system at", datetime.now().strftime("%m-%d-%Y %I:%M %p"))

    if sys.platform == "win32":
        print(Fore.GREEN + "Operating System: ", end="")
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


def getChoice(operatingSystem):
    print("Select operations: ")
    print("1. Times by two")
    print("2. Times by Three")
    print("3. Square")
    print("4. Power of")
    print("")

    if operatingSystem == "Windows":
        choice = str(input("Please type your choice and press \"Enter\" key (Example: 1): "))

        print("")

    elif operatingSystem == "macOS" or operatingSystem == "Linux":
        choice = str(input("Please type your choice and press \"return\" key (Example: 1): "))

        print("")

    return choice


def getNum1(operatingSystem):
    if operatingSystem == "Windows":
        num1 = int(input("Please type a number and press the \"Enter\" key (Example: 2): "))

        print("")

    elif operatingSystem == "macOS" or operatingSystem == "Linux":
        num1 = int(input("Please type a number and press the \"return\" key (Example: 2): "))

        print("")

    return num1


def checkParameters(choice, num1):
    print("Started checking parameters at", datetime.now().strftime("%m-%d-%Y %I:%M %p"))
    valid = "true"

    print("Parameters:")
    print("--------------------------")
    print("choice: {0}".format(choice))
    print("num1  : {0}".format(num1))
    print("--------------------------")

    if choice == None:
        print(Fore.RED + "choice is not set." + Style.RESET_ALL)
        valid = "false"

    if num1 == None:
        print(Fore.RED + "num1 is not set." + Style.RESET_ALL)
        valid = "false"

    if valid == "true":
        print(Fore.GREEN + "All parameter checks passed." + Style.RESET_ALL)

        print("Finished checking parameters at", datetime.now().strftime("%m-%d-%Y %I:%M %p"))
        print("")

    else:
        print(Fore.RED + "One or more parameters are incorrect." + Style.RESET_ALL)

        print("Finished checking parameters at", datetime.now().strftime("%m-%d-%Y %I:%M %p"))
        exit("")


def basicMath():
    print("\nLet's perform basic math in Python.\n")
    operatingSystem = checkOs()

    if len(sys.argv) >= 2:
        choice = str(sys.argv[1])
        num1   = int(sys.argv[2])

    else:
        choice = getChoice(operatingSystem)
        num1   = getNum1(operatingSystem)

    checkParameters(choice, num1)

    try:
        startDateTime = datetime.now()
        print("Started basic math at", startDateTime.strftime("%m-%d-%Y %I:%M %p"))
 
        if choice == '1': 
            def timestwo(x): 
                return x * 2

            print(Fore.BLUE + "{0} times two equals: {1}".format(num1, timestwo(num1)) + Style.RESET_ALL)

        elif choice == '2': 
            def timesthree(x):
                return x * 3

            print(Fore.BLUE + "{0} times three equals: {1}".format(num1, timesthree(num1)) + Style.RESET_ALL) 

        elif choice == '3': 
            def square(x):
                return x * x 

            print(Fore.BLUE + "{0} squared equals: {1}".format(num1, square(num1)) + Style.RESET_ALL)

        elif choice == '4': 
            def power(x, y): 
                return x ** y 
                
            if operatingSystem == "Windows":
                num2 = int(input("Please type the second number and press \"Enter\" key (Example: 2): "))

                print("")

            elif operatingSystem == "macOS" or operatingSystem == "Linux":
                num2 = int(input("Please type the second number and press \"return\" key (Example: 2): "))

                print("")

            print(Fore.BLUE + "{0} to the power of {1} equals: {2}".format(num1, num2, power(num1, num2)) + Style.RESET_ALL)

        else:
            print(Fore.RED + "Invalid input" + Style.RESET_ALL)

        finishedDateTime = datetime.now()
        print("Finished basic math at", finishedDateTime.strftime("%m-%d-%Y %I:%M %p"))

        duration = finishedDateTime - startDateTime
        print("Total execution time: {0} second(s)".format(duration.seconds))
        print("")

    except Exception as e:
        print(Fore.RED + "Failed to perform basic math in Python.")
        print(e)
        print(traceback.print_stack)
        exit("" + Style.RESET_ALL)


basicMath() 
