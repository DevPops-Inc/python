#!/bin/python

# calculate the value of pi with Chudnovsky Algorithm

# you can run this script with: python3 chudnovskyAlgorithmInPython.py < number of decimal places >

import colorama, math, os, sys, traceback
from colorama import Fore, Style
from datetime import datetime
from decimal import Decimal, getcontext
colorama.init()


def checkOs(): 
    print("Started checking operating system at", datetime.now().strftime("%Y-%m-%d %H:%M %p"))

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

    print("Finished checking operating system at", datetime.now().strftime("%Y-%m-%d %H:%M %p"))

    print("")
    return operatingSystem


def getNumberPlaces(operatingSystem):
    if operatingSystem == "Windows": 
        numberPlaces = int(input("Please enter the number of places to calculate Pi to and press \"Enter\" key (Example: 3): "))

        print("")

    elif operatingSystem == "macOS" or operatingSystem == "Linux": 
        numberPlaces = int(input("Please enter the number of places to calculate Pi to and press \"return\" key (Example: 3): "))

        print("")

    return numberPlaces


def checkParameters(numberPlaces): 
    print("Started checking parameters at", datetime.now().strftime("%Y-%m-%d %H:%M %p"))

    valid = "true"

    print("Parameters:")
    print("--------------------------------------")
    print("numberPlaces: {0}".format(numberPlaces))
    print("--------------------------------------")

    if numberPlaces == None: 
        print(Fore.RED + "numberPlaces is not set." + Style.RESET_ALL)
        valid = "false"

    if valid == "true": 
        print(Fore.GREEN + "All parameter checks passed." + Style.RESET_ALL)

        print("Finished checking parameters at", datetime.now().strftime("%Y-%m-%d %H:%M %p"))

        print("")
    else: 
        print(Fore.RED + "One or more paramater checks are incorrect." + Style.RESET_ALL)

        print("Finished checking parameters at", datetime().strftime("%Y-%m-%d %H:%M %p"))

        exit("")


def calculatePi():
    print("\nLet's calculate the value of pi using Chudnovsky's Algorithm.\n")
    operatingSystem = checkOs()

    if len(sys.argv) >= 2: 
        numberPlaces = int(sys.argv[1])

    else: 
        numberPlaces = getNumberPlaces(operatingSystem)

    checkParameters(numberPlaces)

    try: 
        startDateTime = datetime.now()

        print("Started calculating pi at", startDateTime.strftime("%Y-%m-%d %H:%M %p"))

        getcontext().prec = numberPlaces 
        
        def calc(n):
            t = Decimal(0)
            pi = Decimal(0)
            deno = Decimal(0)
            k = 0

            for k in range(n):
                t = (Decimal(-1)**k)*(math.factorial(Decimal(6)*k))*(13591409+545140134*k)
                deno = math.factorial(3*k)*(math.factorial(k)**Decimal(3))*(640320**(3*k))
                pi += Decimal(t)/Decimal(deno)

            pi = pi * Decimal(12)/Decimal(640320**Decimal(1.5))
            pi = 1/pi

            return str(pi)

        print(Fore.BLUE + "The value of pi is: {0}".format(calc(1)) + Style.RESET_ALL)

        finishedDateTime = datetime.now()
        
        print("Finished calculating pi at", finishedDateTime.strftime("%Y-%m-%d %H:%M %p"))

        duration = finishedDateTime - startDateTime
        print("Total execution time: {0} second(s)".format(duration.seconds))
        print("")

    except Exception as e: 
        print(Fore.RED + "Failed to calculate pi.")
        print(e)
        print(traceback.print_stack)
        exit("" + Style.RESET_ALL)


calculatePi()
