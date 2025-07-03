#!/bin/python

# check Fortune in Python 

import colorama, os, sys, subprocess, traceback
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


def checkFortune(): 
    print("\nCheck Fortune in Python.\n")

    try:
        operatingSystem = checkOs()
        
        startDateTime = datetime.now()
        print("Started checking Fortune at", startDateTime.strftime("%m-%d-%Y %I:%M %p"))

        FNULL = open(os.devnull,  'w')

        if operatingSystem == "macOS" or operatingSystem == "Linux":
            checkFortuneOnMacOrLinux = subprocess.call(['which', 'fortune'], stdout=FNULL) 

            if checkFortuneOnMacOrLinux == 0:
                print(Fore.GREEN + "Fortune is installed."+ Style.RESET_ALL)
                print("")

                print("Your fortune is: " + Fore.BLUE)
                os.system('fortune')
                print("")
                print(Fore.GREEN + "Successfully checked Fortune." + Style.RESET_ALL)

                finishedDateTime = datetime.now()

                print("Finished checking Fortune at", finishedDateTime.strftime("%m-%d-%Y %I:%M %p"))

                duration = finishedDateTime - startDateTime
                print("Total execution time: {0} second(s)".format(duration.seconds))
                print("")

            else: 
                raise Exception("Fortune is not installed.")

        elif operatingSystem == "Windows": 
            checkFortuneOnWindows = subprocess.call(['where', 'fortune'], stdout=FNULL)

            if checkFortuneOnWindows == 0:
                print(Fore.GREEN + "Fortune is installed."+ Style.RESET_ALL)
                print("")
                print("Your fortune is: " + Fore.BLUE)
                os.system('fortune')
                print("")
                print(Fore.GREEN + "Successfully checked Fortune." + Style.RESET_ALL)

                finishedDateTime = datetime.now()

                print("Finished checking Fortune at", finishedDateTime.strftime("%m-%d-%Y %I:%M %p"))

                duration = finishedDateTime - startDateTime
                print("Total execution time: {0} second(s)".format(duration.seconds))
                print("")

            else: 
                raise Exception("Fortune is not installed.")
            
    except Exception: 
        print(Fore.RED + "Failed to check Fortune in Python.")
        traceback.print_exc()
        exit("" + Style.RESET_ALL)


checkFortune()
