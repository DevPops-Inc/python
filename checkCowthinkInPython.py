#!/bin/python

# check Cowthink in Python

import colorama, os, sys, subprocess, traceback
from colorama import Fore, Style
from datetime import datetime
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


def checkCowthink(): 
    print("\nCheck Cowthink in Python.\n")
    operatingSystem = checkOs()

    try:
        startDateTime = datetime.now()
        
        print("Started checking Cowthink at", startDateTime.strftime("%Y-%m-%d %H:%M %p"))

        FNULL = open(os.devnull,  'w')

        if operatingSystem == "macOS" or operatingSystem == "Linux":

            checkCowthinkOnMacOrLinux = subprocess.call(['which', 'cowthink'], stdout=FNULL)

            if checkCowthinkOnMacOrLinux == 0:
                os.system('cowthink "Cowthink is installed"')
                print(Fore.GREEN + "Successfully checked Cowthink." + Style.RESET_ALL)

                finishedDateTime = datetime.now()

                print("Finished checking Cowthink at", finishedDateTime.strftime("%Y-%m-%d %H:%M %p"))

                duration = finishedDateTime - startDateTime
                print("Total execution time: {0} second(s)".format(duration.seconds))
                print("")

            else: 
                print(Fore.RED + "Cowthink is not installed." + Style.RESET_ALL)
                
                finishedDateTime = datetime.now()

                print("Finished checking Cowthink at", finishedDateTime.strftime("%Y-%m-%d %H:%M %p"))

                duration = finishedDateTime - startDateTime
                print("Total execution time: {0} second(s)".format(duration.seconds))
                exit("")

        elif operatingSystem == "Windows": 
            
            checkCowthinkOnWindows = subprocess.call(['where', 'cowthink'], stdout=FNULL) 
            
            if checkCowthinkOnWindows == 0:
                os.system('cowthink "Cowthink is installed"')
                print(Fore.GREEN + "Successfully checked Cowthink." + Style.RESET_ALL)

                finishedDateTime = datetime.now()

                print("Finished checking Cowthink at", finishedDateTime.strftime("%Y-%m-%d %H:%M %p"))

                duration = finishedDateTime - startDateTime
                print("Total execution time: {0} second(s)".format(duration.seconds))
                print("")
                
            else: 
                print(Fore.RED + "Cowthink is not installed." + Style.RESET_ALL)
                
                finishedDateTime = datetime.now()

                print("Finished checking Cowthink at", finishedDateTime.strftime("%Y-%m-%d %H:%M %p"))

                duration = finishedDateTime - startDateTime
                print("Total execution time: {0} second(s)".format(duration.seconds))
                exit("")

    except Exception as e: 
        print(Fore.RED + "Failed to check Cowthink in Python.")
        print(e)
        print(traceback.print_stack)
        exit("" + Style.RESET_ALL)


checkCowthink()
