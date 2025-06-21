#!/bin/python

# check Ansible in Python 

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


def checkAnsible(): 
    print("\nCheck Ansible in Python.\n")

    try:
        operatingSystem = checkOs()
        
        startDateTime = datetime.now()
        print("Started checking Ansible at", startDateTime.strftime("%m-%d-%Y %I:%M %p"))

        FNULL = open(os.devnull, 'w')

        if operatingSystem == "macOS" or operatingSystem == "Linux":
            checkAnsibleOnMacOrLinux = subprocess.call(['which', 'ansible'], stdout=FNULL) 

            if checkAnsibleOnMacOrLinux == 0:
                print(Fore.GREEN + "Ansible is installed."+ Style.RESET_ALL)
                os.system('ansible --version')
                print(Fore.GREEN + "Successfully checked Ansible." + Style.RESET_ALL)

                finishedDateTime = datetime.now()

                print("Finished checking Ansible at", finishedDateTime.strftime("%m-%d-%Y %I:%M %p"))

                duration = finishedDateTime - startDateTime
                print("Total execution time: {0} second(s)".format(duration.seconds))
                print("")

            else: 
                raise Exception("Ansible is not installed.")

        elif operatingSystem == "Windows": 
            checkAnsibleOnWindows = subprocess.call(['where', 'ansible'], stdout=FNULL)

            if checkAnsibleOnWindows == 0:
                print(Fore.GREEN + "Ansible is installed."+ Style.RESET_ALL)
                os.system('ansible --version')
                print(Fore.GREEN + "Successfully checked Ansible." + Style.RESET_ALL)

                finishedDateTime = datetime.now()

                print("Finished checking Ansible at", finishedDateTime.strftime("%m-%d-%Y %I:%M %p"))

                duration = finishedDateTime - startDateTime
                print("Total execution time: {0} second(s)".format(duration.seconds))
                print("")

            else: 
                raise Exception("Ansible is not installed.")
                
    except Exception: 
        print(Fore.RED + "Failed to check Ansible in Python.")
        traceback.print_exc()
        exit("" + Style.RESET_ALL)


checkAnsible()
