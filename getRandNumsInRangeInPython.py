#!/bin/python

# get random numbers in range in Python

# you can run this script with: python3 getRandNumInRangeInPython.py < begin number range > < end number range > < number of random numbers > 

import colorama, os, random, sys, time, traceback
from colorama import Fore, Style
from datetime import datetime
colorama.init()


def checkOs(): 
    print("Started checking operating system at", datetime.now().strftime("%m-%d-%Y %I:%M %p"))

    if sys.platform == "win32": 
        print(Fore.GREEN + "Operating System:", end="")
        os.system('ver')
        print(Style.RESET_ALL, end="")
        operatingSystem = "Windows"

    elif sys.platform == "darwin": 
        print(Fore.GREEN + "Operating System:")
        os.system('sw_vers')
        print(Style.RESET_ALL, end="")
        operatingSystem = "macOS"

    elif sys.platform == "linux": 
        print(Fore.GREEN + "Operating System:")
        os.system('uname -r')
        print(Style.RESET_ALL)
        operatingSystem = "Linux"

    print("Finished checking operating system at", datetime.now().strftime("%m-%d-%Y %I:%M %p")) 

    print("")
    return operatingSystem


def getBeginNumRange(operatingSystem): 
    if operatingSystem == "Windows": 
        beginNumRange = int(input("Please type the beginning of the number range and press the \"Enter\" key (Example: 1): "))

    else: 
        beginNumRange = int(input("Please type the beginning of the number range and press the \"return\" key (Example: 1): "))

    print("")
    return beginNumRange


def getEndNumRange(operatingSystem): 
    if operatingSystem == "Windows": 
        endNumRange = int(input("Please type the ending of the number range and press the \"Enter\" key (Example: 25): "))

    else: 
        endNumRange = int(input("Please type the ending of the number range and press the \"return\" key (Example: 25): "))

    print("")
    return endNumRange


def getNumRandomNum(operatingSystem): 
    if operatingSystem == "Windows": 
        numRandomNum = int(input("Please type how many random numbers you want to get (Example: 10): "))

    else: 
        numRandomNum = int(input("Please type how many random numbers you want to get (Example: 10): "))
        
    print("")
    return numRandomNum


def checkParameters(beginNumRange, endNumRange, numRandomNum): 
    print("Started checking parameter(s) at", datetime.now().strftime("%m-%d-%Y %I:%M %p"))
    valid = True

    print("Parameter(s):")
    print("----------------------------------------")
    print("beginNumRange: {0}".format(beginNumRange))
    print("endNumRange  : {0}".format(endNumRange))
    print("numRandomNum : {0}".format(numRandomNum))
    print("----------------------------------------")

    if beginNumRange == None or beginNumRange == "": 
        print(Fore.RED + "beginNumRange is not set." + Style.RESET_ALL)
        valid = False

    if endNumRange == None or endNumRange == "": 
        print(Fore.RED + "endNumRange is not set." + Style.RESET_ALL)
        valid = False

    if numRandomNum == None or numRandomNum == "": 
        print(Fore.RED + "numRandomNum is not set." + Style.RESET_ALL)
        valid = False

    if valid == True: 
        print(Fore.GREEN + "All parameter check(s) passed." + Style.RESET_ALL)

        print("Finished checking parameter(s) at", datetime.now().strftime("%m-%d-%Y %I:%M %p"))
        print("")

    else: 
        raise Exception("One or more parameters are incorrect.")


def getRandomNumsInRange(): 
    print("\nGet random numbers in range in Python.\n")
    operatingSystem = checkOs()

    if len(sys.argv) >= 2: 
        beginNumRange = int(sys.argv[1])
        endNumRange   = int(sys.argv[2])
        numRangeNum   = int(sys.argv[3])

    else: 
        beginNumRange = getBeginNumRange(operatingSystem)
        endNumRange   = getEndNumRange(operatingSystem)
        numRangeNum   = getNumRandomNum(operatingSystem)

    checkParameters(beginNumRange, endNumRange, numRangeNum)

    try: 
        startDateTime = datetime.now()
        
        print("Started getting random numbers in range at", startDateTime.strftime("%m-%d-%Y %I:%M %p"))

        print(Fore.BLUE + "Here are {0} random numbers between {1} and {2}:".format(numRangeNum, beginNumRange, endNumRange))

        for i in range(numRangeNum):
            time.sleep(.25)
            print(random.randint(beginNumRange, endNumRange))

        print(Fore.GREEN + "Successfully got random numbers in range." + Style.RESET_ALL)

        finishedDateTime = datetime.now()

        print("Finished getting random numbers in range at", finishedDateTime.strftime("%m-%d-%Y %I:%M %p"))

        duration = finishedDateTime - startDateTime
        print("Total execution time: {0} second(s)".format(duration.seconds))
        print("")

    except Exception: 
        print(Fore.RED + "Failed to get random numbers in range.")
        traceback.print_exc()
        exit("" + Style.RESET_ALL)


getRandomNumsInRange()
