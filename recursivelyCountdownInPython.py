#!/bin/python

# recursively countdown in Python 

# you can run this script with: python3 recursivelyCountdownInPython.py < countdown number >

import colorama, os, sys, time, traceback
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
        print(Fore.GREEN + "Operating Systmem:")
        os.system('uname -r')
        print(Style.RESET_ALL, end="")
        operatingSystem = "Linux"

    print("Finished checking operating system at", datetime.now().strftime("%m-%d-%Y %I:%M %p"))

    print("")
    return operatingSystem


def getCountdownNum(operatingSystem): 
    if sys.platform == "Windows": 

        countdownNum = int(input("Please type the number you would like to countdown from and press the \"Enter\" key (Example: 5): "))

    else: 

        countdownNum = int(input("Please type the number you would like to countdown from and press the \"Enter\" key (Example: 5): "))

    print("")
    return countdownNum


def checkParameters(countdownNum): 
    print("Started checking parameter(s) at", datetime.now().strftime("%m-%d-%Y %I:%M %p"))
    valid = True

    print("Parameter(s):")
    print("--------------------------------------")
    print("countdownNum: {0}".format(countdownNum))
    print("--------------------------------------")

    if countdownNum == None or countdownNum == "": 
        print(Fore.RED + "countdownNum is not set." + Style.RESET_ALL)
        valid = False 

    if valid == True: 
        print(Fore.GREEN + "All parameter check(s) passed." + Style.RESET_ALL)

        print("Finished checking parameters at", datetime.now().strftime("%m-%d-%Y %I:%M %p"))
        print("")

    else: 
        raise Exception("One or more parameters are incorrect.")


def countdown(countdownNum):
    if (countdownNum < 0): 
        raise Exception("Sorry can't countdown from below zero.")
    
    elif (countdownNum == 0):
        print(Fore.GREEN)

    else:
        print(Fore.BLUE)
        print(countdownNum, end="")
        time.sleep(.5)
        countdown(countdownNum-1)


def recursivelyCountdown(): 
    print("\nLet's recursively countdown in Python!\n")

    try:
        operatingSystem = checkOs()

        if len(sys.argv) >= 2: 
            countdownNum = int(sys.argv[1])

        else: 
            countdownNum = getCountdownNum(operatingSystem)

        checkParameters(countdownNum)
        
        startDateTime = datetime.now()

        print("Started recursively counting down at {0}".format(startDateTime.strftime("%m-%d-%Y %I:%M %p")), end="")

        countdown(countdownNum)

        print(Fore.GREEN + "Successfully counted down from {0}.".format(countdownNum) + Style.RESET_ALL)

        finishedDateTime = datetime.now()
        
        print("Finished recursively counting down at", finishedDateTime.strftime("%m-%d-%Y %I:%M %p"))

        duration = finishedDateTime - startDateTime
        print("Total execution time: {0} second(s)".format(duration.seconds))
        print("")

    except Exception: 
        print(Fore.RED + "Failed to recursively countdown.")
        traceback.print_exc()
        exit("" + Style.RESET_ALL)


recursivelyCountdown()
