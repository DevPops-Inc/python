#!/bin/python

# first recurring character in Python 

# you can run this script with: python3 firstRecurringCharInPython.py "< random string >"

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


def getRandomString(operatingSystem): 
    if operatingSystem == "Windows": 
        randomString = str(input("Please type a random string and press the \"Enter\" key (Example: only test in prod): "))

    else: 
        randomString = str(input("Please type a random string and press the \"return\" key (Example: only test in prod): "))

    print("")
    return randomString


def checkParameters(randomString): 
    print("Started checking parameter(s) at", datetime.now().strftime("%m-%d-%Y %I:%M %p"))
    valid = True

    print("Parameter(s):")
    print("--------------------------------------")
    print("randomString: {0}".format(randomString))
    print("--------------------------------------")

    if randomString == None or randomString == "": 
        print(Fore.RED + "randomString is not set." + Style.RESET_ALL)
        valid = False

    if valid == True: 
        print(Fore.GREEN + "All parameter checks passed." + Style.RESET_ALL)

        print("Finished checking parameter(s) at", datetime.now().strftime("%m-%d-%Y %I:%M %p"))
        print("")

    else: 
        raise Exception("One or more parameters are incorrect.")


def firstRecurringChar(): 
    print("\nFirst recurring character in Python\n")

    try: 
        operatingSystem = checkOs()

        if len(sys.argv) >= 2: 
            randomString = str(sys.argv[1])

        else: 
            randomString = getRandomString(operatingSystem)

        checkParameters(randomString)
        
        startDateTime = datetime.now()
        
        print("Started finding first recurring character at", startDateTime.strftime("%m-%d-%Y %I:%M %p"))

        h = {}

        def firstRecur(str): 
            for ch in str: 
                if ch in h: 
                    return ch; 
                else: 
                    h[ch] = 0
            return '\0'

        print(Fore.BLUE + "The first recurring character is:", firstRecur(randomString))
        print(Fore.GREEN + "Successfully found the first recurring character." + Style.RESET_ALL)

        finishedDateTime = datetime.now()
        
        print("Finished finding first recurring character at", finishedDateTime.strftime("%m-%d-%Y %I:%M %p"))

        duration = finishedDateTime - startDateTime
        print("Total execution timne: {0} second(s)".format(duration.seconds))
        print("")

    except Exception: 
        print(Fore.RED + "Failed to find first recurring character.")
        traceback.print_exc()
        exit("" + Style.RESET_ALL)


firstRecurringChar()
