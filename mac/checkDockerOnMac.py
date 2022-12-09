#!/bin/python

# check Docker on Mac

import colorama, os, subprocess, sys, traceback
from colorama import Fore, Style
from datetime import datetime
colorama.init()


def checkOsForMac(): 
    print("Started checking operating system at", datetime.now().strftime("%m-%d-%Y %I:%M %p"))

    if sys.platform == "darwin": 
        print(Fore.GREEN + "Operating System: ")
        os.system('sw_vers')
        print(Style.RESET_ALL, end="")

        print("Finished checking operating system at", datetime.now().strftime("%m-%d-%Y %I:%M %p"))
        print("")

    else: 
        print(Fore.RED + "Sorry but this script only runs on Mac." + Style.RESET_ALL)

        print("Finished checking operating system at", datetime.now().strftime("%m-%d-%Y %I:%M %p"))
        print("")

        
def checkDocker(): 
    print("\nCheck Docker on Mac.\n")
    checkOsForMac()

    try: 
        startDateTime = datetime.now()
        print("Started checking Docker at", startDateTime.strftime("%m-%d-%Y %I:%M %p"))

        FNULL = open(os.devnull, 'w')
        checkDockerOnMac = subprocess.call(['which', 'brew'], stdout=FNULL)

        if checkDockerOnMac == 0: 
            print(Fore.GREEN + "Docker is installed." + Style.RESET_ALL)
            os.system('docker --version')

        else: 
            print(Fore.RED + "Docker is not installed.")

        print(Fore.GREEN + "Successfully checked Docker." + Style.RESET_ALL)
        
        finishedDateTime = datetime.now()
        print("Finished checking Docker at", finishedDateTime.strftime("%m-%d-%Y %I:%M %p"))

        duration = finishedDateTime - startDateTime
        print("Total execution time: {0} second(s)".format(duration.seconds))
        print("")

    except Exception as e: 
        print(Fore.RED + "Failed to check Docker.")
        print(e)
        print(traceback.print_stack)
        exit("" + Style.RESET_ALL)

checkDocker()
