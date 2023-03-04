#!/bin/python

# check argcomplete in Python 

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


def checkArgcomplete(): 
    print("\nCheck argcomplete in Python.\n")
    operatingSystem = checkOs()

    try:
        startDateTime = datetime.now()
        print("Started checking argcomplete at", startDateTime.strftime("%m-%d-%Y %I:%M %p"))

        FNULL = open(os.devnull, 'w')

        if operatingSystem == "macOS" or operatingSystem == "Linux":

            checkArgcompleteOnMacOrLinux = subprocess.call(['which', 'argcomplete'], stdout=FNULL) 

            if checkArgcompleteOnMacOrLinux == 0:
                print(Fore.GREEN + "argcomplete is installed."+ Style.RESET_ALL)
                os.system('argcomplete --version')
                print(Fore.GREEN + "Successfully checked argcomplete." + Style.RESET_ALL)

                finishedDateTime = datetime.now()

                print("Finished checking argcomplete at", finishedDateTime.strftime("%m-%d-%Y %I:%M %p"))

                duration = finishedDateTime - startDateTime
                print("Total execution time: {0} second(s)".format(duration.seconds))
                print("")

            else: 
                print(Fore.RED + "argcomplete is not installed." + Style.RESET_ALL)
                
                finishedDateTime = datetime.now()

                print("Finished checking argcomplete at", finishedDateTime.strftime("%m-%d-%Y %I:%M %p"))

                duration = finishedDateTime - startDateTime
                print("Total execution time: {0} second(s)".format(duration.seconds))
                exit("")

        elif operatingSystem == "Windows": 
            checkArgcompleteOnWindows = subprocess.call(['where', 'argcomplete'], stdout=FNULL)

            if checkArgcompleteOnWindows == 0:
                print(Fore.GREEN + "argcomplete is installed."+ Style.RESET_ALL)
                os.system('argcomplete --version')
                print(Fore.GREEN + "Successfully checked argcomplete." + Style.RESET_ALL)

                finishedDateTime = datetime.now()

                print("Finished checking argcomplete at", finishedDateTime.strftime("%m-%d-%Y %I:%M %p"))

                duration = finishedDateTime - startDateTime
                print("Total execution time: {0} second(s)".format(duration.seconds))
                print("")

            else: 
                print(Fore.RED + "argcomplete is not installed." + Style.RESET_ALL)
                
                finishedDateTime = datetime.now()

                print("Finished checking argcomplete at", finishedDateTime.strftime("%m-%d-%Y %I:%M %p"))

                duration = finishedDateTime - startDateTime
                print("Total execution time: {0} second(s)".format(duration.seconds))
                exit("")
                
    except Exception: 
        print(Fore.RED + "Failed to check argcomplete in Python.")
        traceback.print_exc()
        exit("" + Style.RESET_ALL)


checkArgcomplete()
