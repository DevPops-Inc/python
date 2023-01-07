#!/bin/python

# check PIP in Python 

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


def checkPip(): 
    print("\nCheck PIP in Python.\n")
    operatingSystem = checkOs()

    try:
        startDateTime = datetime.now()
        
        print("Started checking PIP at", startDateTime.strftime("%m-%d-%Y %I:%M %p"))

        FNULL = open(os.devnull,  'w')

        if operatingSystem == "macOS" or operatingSystem == "Linux":

            checkPipOnMacOrLinux = subprocess.call(['which', 'pip'], stdout=FNULL) 

            if checkPipOnMacOrLinux == 0:
                print(Fore.GREEN + "PIP is installed."+ Style.RESET_ALL)
                os.system('pip --version')
                print(Fore.GREEN + "Successfully checked PIP." + Style.RESET_ALL)

                finishedDateTime = datetime.now()

                print("Finished checking PIP at", finishedDateTime.strftime("%m-%d-%Y %I:%M %p"))

                duration = finishedDateTime - startDateTime
                print("Total execution time: {0} second(s)".format(duration.seconds))
                print("")

            else: 
                print(Fore.RED + "PIP is not installed." + Style.RESET_ALL)
                
                finishedDateTime = datetime.now()

                print("Finished checking PIP at", finishedDateTime.strftime("%m-%d-%Y %I:%M %p"))

                duration = finishedDateTime - startDateTime
                print("Total execution time: {0} second(s)".format(duration.seconds))
                exit("")

        elif operatingSystem == "Windows": 
            
            checkPipOnWindows = subprocess.call(['where', 'pip'], stdout=FNULL)

            if checkPipOnWindows == 0:
                print(Fore.GREEN + "PIP is installed."+ Style.RESET_ALL)
                os.system('pip --version')
                print(Fore.GREEN + "Successfully checked PIP." + Style.RESET_ALL)

                finishedDateTime = datetime.now()

                print("Finished checking PIP at", finishedDateTime.strftime("%m-%d-%Y %I:%M %p"))

                duration = finishedDateTime - startDateTime
                print("Total execution time: {0} second(s)".format(duration.seconds))
                print("")

            else: 
                print(Fore.RED + "PIP is not installed." + Style.RESET_ALL)
                
                finishedDateTime = datetime.now()

                print("Finished checking PIP at", finishedDateTime.strftime("%m-%d-%Y %I:%M %p"))

                duration = finishedDateTime - startDateTime
                print("Total execution time: {0} second(s)".format(duration.seconds))
                exit("")
                
    except Exception as e: 
        print(Fore.RED + "Failed to check PIP in Python.")
        print(e)
        print(traceback.print_stack)
        exit("" + Style.RESET_ALL)


checkPip()
