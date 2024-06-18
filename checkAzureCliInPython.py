#!/bin/python

# check Azure CLI in Python 

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


def checkAzureCli(): 
    print("\nCheck Azure CLI in Python.\n")
    operatingSystem = checkOs()

    try:
        startDateTime = datetime.now()
        print("Started checking Azure CLI at", startDateTime.strftime("%m-%d-%Y %I:%M %p"))

        FNULL = open(os.devnull, 'w')

        if operatingSystem == "macOS" or operatingSystem == "Linux":
            checkAzureCliOnMacOrLinux = subprocess.call(['which', 'az'], stdout=FNULL) 

            if checkAzureCliOnMacOrLinux == 0:
                print(Fore.GREEN + "Azure CLI is installed."+ Style.RESET_ALL)
                os.system('az --version')
                print(Fore.GREEN + "Successfully checked Azure CLI." + Style.RESET_ALL)

                finishedDateTime = datetime.now()

                print("Finished checking Azure CLI at", finishedDateTime.strftime("%m-%d-%Y %I:%M %p"))

                duration = finishedDateTime - startDateTime
                print("Total execution time: {0} second(s)".format(duration.seconds))
                print("")

            else: 
                raise Exception("Azure CLI is not installed.")

        elif operatingSystem == "Windows": 
            checkAzureCliOnWindows = subprocess.call(['where', 'az'], stdout=FNULL)

            if checkAzureCliOnWindows == 0:
                print(Fore.GREEN + "Azure CLI is installed."+ Style.RESET_ALL)
                os.system('az --version')
                print(Fore.GREEN + "Successfully checked Azure CLI." + Style.RESET_ALL)

                finishedDateTime = datetime.now()

                print("Finished checking Azure CLI at", finishedDateTime.strftime("%m-%d-%Y %I:%M %p"))

                duration = finishedDateTime - startDateTime
                print("Total execution time: {0} second(s)".format(duration.seconds))
                print("")

            else: 
                raise Exception("Azure CLI is not installed.")
                
    except Exception: 
        print(Fore.RED + "Failed to check Azure CLI in Python.")
        traceback.print_exc()
        exit("" + Style.RESET_ALL)


checkAzureCli()
