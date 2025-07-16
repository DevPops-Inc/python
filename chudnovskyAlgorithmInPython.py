#!/bin/python

# calculate the value of pi with Chudnovsky Algorithm

# you can run this script with: python3 chudnovskyAlgorithmInPython.py < number places >

import colorama, math, os, sys, traceback
from colorama import Fore, Style
from datetime import datetime
from decimal import Decimal, getcontext
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


def getNumPlaces(operatingSystem):
    if operatingSystem == "Windows": 
        numPlaces = int(input("Please enter the number of places to calculate Pi to and press \"Enter\" key (Example: 3): "))

    elif operatingSystem == "macOS" or operatingSystem == "Linux": 
        numPlaces = int(input("Please enter the number of places to calculate Pi to and press \"return\" key (Example: 3): "))

    print("")
    return numPlaces


def checkParameters(numPlaces): 
    print("Started checking parameter(s) at", datetime.now().strftime("%m-%d-%Y %I:%M %p"))

    valid = True

    print("Parameter(s):")
    print("--------------------------------")
    print("numPlaces: {0}".format(numPlaces))
    print("--------------------------------")

    if numPlaces == None or numPlaces == "": 
        print(Fore.RED + "numPlaces is not set." + Style.RESET_ALL)
        valid = False

    if valid == True: 
        print(Fore.GREEN + "All parameter check(s) passed." + Style.RESET_ALL)

        print("Finished checking parameter(s) at", datetime.now().strftime("%m-%d-%Y %I:%M %p"))
        print("")
    else: 
        raise Exception("One or more paramater checks are incorrect.")


def calculatePi():
    print("\nLet's calculate the value of pi using Chudnovsky's Algorithm.\n")

    try: 
        operatingSystem = checkOs()

        if len(sys.argv) >= 2: 
            numPlaces = int(sys.argv[1])

        else: 
            numPlaces = getNumPlaces(operatingSystem)

        checkParameters(numPlaces)

        startDateTime = datetime.now()
        print("Started calculating pi at", startDateTime.strftime("%m-%d-%Y %I:%M %p"))

        getcontext().prec = numPlaces 
        
        def calc(n):
            t = Decimal(0)
            pi = Decimal(0)
            deno = Decimal(0)
            k = 0

            for k in range(n):
                t = (Decimal(-1)**k)*(math.factorial(int(Decimal(6)*k)))*(13591409+545140134*k)
                deno = math.factorial(3*k)*(math.factorial(k)**Decimal(3))*(640320**(3*k))
                pi += Decimal(t)/Decimal(deno)

            pi = pi * Decimal(12)/Decimal(640320**Decimal(1.5))
            pi = 1/pi

            return str(pi)

        print(Fore.BLUE + "The value of pi is: {0}".format(calc(1)) + Style.RESET_ALL)

        finishedDateTime = datetime.now()
        print("Finished calculating pi at", finishedDateTime.strftime("%m-%d-%Y %I:%M %p"))

        duration = finishedDateTime - startDateTime
        print("Total execution time: {0} second(s)".format(duration.seconds))
        print("")

    except Exception: 
        print(Fore.RED + "Failed to calculate pi.")
        traceback.print_exc()
        exit("" + Style.RESET_ALL)


calculatePi()
