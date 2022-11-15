#!/bin/python

# check Cowsay in Python

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


def checkCowsay(): 
    print("\nCheck Cowsay in Python.\n")
    operatingSystem = checkOs()

    try:
        startDateTime = datetime.now()
        
        print("Started checking Cowsay at", startDateTime.strftime("%Y-%m-%d %H:%M %p"))

        FNULL = open(os.devnull, 'w')

        if operatingSystem == "macOS" or operatingSystem == "Linux":

            checkCowsayOnMacOrLinux = subprocess.call(['which', 'cowsay'], stdout=FNULL)

            if checkCowsayOnMacOrLinux == 0:
                os.system('cowsay "Cowsay is installed"')
                print(Fore.GREEN + "Successfully checked Cowsay." + Style.RESET_ALL)

                finishedDateTime = datetime.now()

                print("Finished checking Cowsay at", finishedDateTime.strftime("%Y-%m-%d %H:%M %p"))

                duration = finishedDateTime - startDateTime
                print("Total execution time: {0} second(s)".format(duration.seconds))
                print("")

            else: 
                print(Fore.RED + "Cowsay is not installed." + Style.RESET_ALL)
                
                finishedDateTime = datetime.now()

                print("Finished checking Cowsay at", finishedDateTime.strftime("%Y-%m-%d %H:%M %p"))

                duration = finishedDateTime - startDateTime
                print("Total execution time: {0} second(s)".format(duration.seconds))
                exit("")

        elif operatingSystem == "Windows": 
            
            checkCowsayOnWindows = subprocess.call(['where', 'cowsay'], stdout=FNULL) 
            
            if checkCowsayOnWindows == 0:
                os.system('cowsay "Cowsay is installed"')
                print(Fore.GREEN + "Successfully checked Cowsay." + Style.RESET_ALL)

                finishedDateTime = datetime.now()

                print("Finished checking Cowsay at", finishedDateTime.strftime("%Y-%m-%d %H:%M %p"))

                duration = finishedDateTime - startDateTime
                print("Total execution time: {0} second(s)".format(duration.seconds))
                print("")
                
            else: 
                print(Fore.RED + "Cowsay is not installed." + Style.RESET_ALL)
                
                finishedDateTime = datetime.now()

                print("Finished checking Cowsay at", finishedDateTime.strftime("%Y-%m-%d %H:%M %p"))

                duration = finishedDateTime - startDateTime
                print("Total execution time: {0} second(s)".format(duration.seconds))
                exit("")

    except Exception as e: 
        print(Fore.RED + "Failed to check Cowsay in Python.")
        print(e)
        print(traceback.print_stack)
        exit("" + Style.RESET_ALL)


checkCowsay()
