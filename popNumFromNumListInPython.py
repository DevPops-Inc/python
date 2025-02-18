#!/bin/python

# pop number from number list in Python

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


def createNumList(operatingSystem):
    numberList = []

    if operatingSystem == "Windows": 

        numList = int(input("Please type the number of items in the list and press the \"Enter\" key (Example: 4): "))

        print("")

        def addNumToListOnWin(numList): 
            if numList > 0: 

                addItem = int(input("Please type a number you wish to add to the list and press the \"Enter\" key (Example: 1): "))

                numberList.append(addItem)
                addNumToListOnWin(numList-1)

        addNumToListOnWin(numList)

    else: 

        numList = int(input("Please type the number of items in your list and press the \"return\" key (Example: 4): "))

        print("")

        def addNumToListOnMacOrLinux(numList): 
            if numList > 0: 

                addItem = int(input("Please type a number you wish to add to the list and press the \"return\" key (Example: 1): "))

                numberList.append(addItem)
                addNumToListOnMacOrLinux(numList-1)

        addNumToListOnMacOrLinux(numList)

    print("")
    return numberList


def getPopNum(numberList, operatingSystem): 
    print(Fore.BLUE + "The number list is: {0}".format(numberList) + Style.RESET_ALL)

    if operatingSystem == "Windows": 

        popNum = int(input("Please type the index (starting from zero) you wish to pop from the number list and press the \"Enter\" key: "))

    else: 

        popNum = int(input("Please type the index (starting from zero) you wish to pop from the number list and press the \"return\" key: "))
    
    print("")
    return popNum


def checkParameters(numberList, popNum): 
    print("Started checking parameter(s) at", datetime.now().strftime("%m-%d-%Y %I:%M %p"))
    valid = True 

    print("Parameter(s):")
    print("----------------------------------")
    print("numberList: {0}".format(numberList))
    print("popNum    : {0}".format(popNum))
    print("----------------------------------")

    if numberList == None or numberList == "": 
        print(Fore.RED + "numberList is not set." + Style.RESET_ALL)
        valid = False

    if popNum == None or popNum == "": 
        print(Fore.RED + "popNum is not set." + Style.RESET_ALL)
        valid = False 

    if valid == True: 
        print(Fore.GREEN + "All parameter check(s) passed." + Style.RESET_ALL)

        print("Finished checking parameter(s) at", datetime.now().strftime("%m-%d-%Y %I:%M %p"))

        print("")

    else: 
        raise Exception("One or more parameters are incorrect.")


def popNumFromNumList(): 
    print("\nPop number from number list in Python.\n")

    operatingSystem = checkOs()
    numberList      = createNumList(operatingSystem)
    popNum          = getPopNum(numberList, operatingSystem)
    
    try:
        checkParameters(numberList, popNum)

        startDateTime = datetime.now()

        print("Started popping item from number list at", startDateTime.strftime("%m-%d-%Y %I:%M %p"))

        numberList.pop(popNum)
        print(Fore.BLUE + "The number list is now: {0}".format(numberList))
        print(Fore.GREEN + "Successfully popped item from number list." + Style.RESET_ALL)

        finishedDateTime = datetime.now()
        
        print("Finished popping item from number list at", finishedDateTime.strftime("%m-%d-%Y %I:%M %p"))

        duration = finishedDateTime - startDateTime
        print("Total execution time: {0} second(s)".format(duration.seconds))
        print("")

    except Exception: 
        print(Fore.RED + "Failed to pop item from number list.")
        traceback.print_exc()
        exit("" + Style.RESET_ALL)


popNumFromNumList()
