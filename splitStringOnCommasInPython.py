#!/bin/python 

# split string on commas in Python 

# you can run this script with: python3 splitStringOnCommasInPython.py "< string with commas >"

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
        print(Fore.GREEN + "Operating System:")
        os.system('sw_vers')
        print(Style.RESET_ALL, end="")
        operatingSystem = "macOS"

    elif sys.platform == "linux": 
        print(Fore.GREEN + "Operating System:")
        os.system('uname -r')
        print(Style.RESET_ALL, end="")
        operatingSystem = "Linux"

    print("Finished checking operating system at", datetime.now().strftime("%m-%d-%Y %I:%M %p"))
    print("")
    return operatingSystem


def getStringWithCommas(operatingSystem): 
    if sys.platform == "Windows": 

        stringWithCommas = str(input("Please type a string with commas and press the \"Enter\" (Example: string, with, commas): "))

    else: 
        
        stringWithCommas = str(input("Please type a string with commas and press the \"return\" (Example: string, with, commas): "))
    
    print("")
    return stringWithCommas


def checkParameters(stringWithCommas): 
    print("Started checking parameter(s) at", datetime.now().strftime("%m-%d-%Y %I:%M %p"))
    valid = True 

    print("Parameter(s):")
    print("----------------------------------------------")
    print("stringWithCommas: {0}".format(stringWithCommas))
    print("----------------------------------------------")

    if stringWithCommas == None or stringWithCommas == "": 
        print(Fore.RED + "stringWithCommas is not set." + Style.RESET_ALL)
        valid = False 

    if valid == True: 
        print(Fore.GREEN + "All parameter check(s) passed." + Style.RESET_ALL)

        print("Finished checking parameter(s) at", datetime.now().strftime("%m-%d-%Y %I:%M %p"))
        print("")

    else: 
        raise Exception(Fore.RED + "One or more parameter check(s) are incorrect.")


def splitStringOnCommas(): 
    print("\nSplit string on commas in Python.\n")
    operatingSystem = checkOs()

    if len(sys.argv) >= 2: 
        stringWithCommas = str(sys.argv[1])

    else: 
        stringWithCommas = getStringWithCommas(operatingSystem)

    checkParameters(stringWithCommas)

    try: 
        startDateTime = datetime.now()
        
        print("Started splitting string on commas at", startDateTime.strftime("%m-%d-%Y %I:%M %p"))

        if "," in stringWithCommas: 
            splitStringWithCommas=stringWithCommas.split(",")
            print(Fore.BLUE, end="")
            print(splitStringWithCommas)
            print(Fore.GREEN + "Successfully split string on commas." + Style.RESET_ALL)

        else: 
            raise Exception("There are no commas in this string.")

        finishedDateTime = datetime.now()

        print("Finished splitting string on commas at", finishedDateTime.strftime("%m-%d-%Y %I:%M %p"))

        duration = finishedDateTime - startDateTime
        print("Total execution time: {0} second(s)".format(duration.seconds))
        print("")

    except Exception: 
        print(Fore.RED + "Failed to split string on commas.")
        traceback.print_exc()
        exit("" + Style.RESET_ALL)


splitStringOnCommas()
