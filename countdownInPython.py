#!/bin/python

# countdown in Python

# you can run this script with: python3 countdownInPython.py < countdown number > 

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
        print(Style.RESET_ALL)
        operatingSystem = "macOS"

    elif sys.platform == "linux": 
        os.system(unamme -r)
        print(Style.RESET_ALL)
        operatingSystem = "Linux"

    print("Finished checking operating system at", datetime.now().strftime("%m-%d-%Y %I:%M %p"))

    print("")
    return operatingSystem


def getCountdownNumber(operatingSystem): 
    if operatingSystem == "Windows": 
        countdownNum = int(input("Please type the number you wish to countdown from and press the \"Enter\" key (Example: 5): "))

    else: 
        countdownNum = int(input("Please type the number you wish to countdown from and press the \"return\" key (Example: 5): "))

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

        print("Finished checking parameter(s) at", datetime.now().strftime("%m-%d-%Y %I:%M %p"))
        print("")

    else: 
        raise Exception("One or more parameter checks are incorrect.")


def countdown():
    print("\nLet's countdown in Python!\n")
    operatingSystem = checkOs()

    if len(sys.argv) >= 2: 
        countdownNum = int(sys.argv[1])

    else: 
        countdownNum = getCountdownNumber(operatingSystem)

    checkParameters(countdownNum)

    try: 
        startDateTime = datetime.now()
        print("Started counting down at", startDateTime.strftime("%m-%d-%Y %I:%M %p"))

        if countdownNum > 0: 
            while countdownNum > 0:
                print(Fore.BLUE, end=""); sys.stdout.flush()
                print(countdownNum)
                countdownNum = countdownNum -1
                time.sleep(.5)
                
        else: 
            raise Exception("Sorry but can't countdown from zero or below.")
            
        print(Fore.GREEN + "Successfully counted down." + Style.RESET_ALL)

        finishedDateTime = datetime.now()
        print("Finished counting down at", finishedDateTime.strftime("%m-%d-%Y %I:%M %p"))

        duration = finishedDateTime - startDateTime
        print("Total execution time: {0} second(s)".format(duration.seconds))
        print("")

    except Exception: 
        print(Fore.RED + "Failed countdown.")
        traceback.print_exc()
        exit("" + Style.RESET_ALL)


countdown()
