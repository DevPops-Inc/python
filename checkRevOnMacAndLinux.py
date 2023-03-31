#!/bin/python

# check rev on Mac and Linux

import colorama, os, sys, subprocess, traceback
from colorama import Fore, Style
from datetime import datetime
colorama.init()


def checkOsForMacOrLinux():
    print("Started checking operating system at", datetime.now().strftime("%m-%d-%Y %I:%M %p"))

    if sys.platform == "darwin": 
        print(Fore.GREEN + "Operating System: ")
        os.system('sw_vers')
        print(Style.RESET_ALL, end="")

    elif sys.platform == "linux": 
        print(Fore.GREEN + "Operating System: ")
        os.system('uname -r')
        print(Style.RESET_ALL, end="")

    else: 
        print(Fore.RED + "Sorry but this only runs on Mac or Linux." + Style.RESET_ALL)

        print("Finished checking operating system at", datetime.now().strftime("%m-%d-%Y %I:%M %p)"))

        exit("")
    
    print("Finished checking operating system at", datetime.now().strftime("%m-%d-%Y %I:%M %p"))
    print("")


def checkRev(): 
    print("\nCheck rev on Mac.\n")
    checkOsForMacOrLinux()

    try:
        startDateTime = datetime.now()
        print("Started checking rev at", startDateTime.strftime("%m-%d-%Y %I:%M %p"))

        FNULL = open(os.devnull,  'w')

        checkAnsibleOnMacOrLinux = subprocess.call(['which', 'rev'], stdout=FNULL) 

        if checkAnsibleOnMacOrLinux == 0:
            print(Fore.GREEN + "rev is installed." + Fore.BLUE)
            os.system('echo "rev is installed." | rev')
            print(Fore.GREEN + "Successfully checked rev." + Style.RESET_ALL)

            finishedDateTime = datetime.now()

            print("Finished checking rev at", finishedDateTime.strftime("%m-%d-%Y %I:%M %p"))

            duration = finishedDateTime - startDateTime
            print("Total execution time: {0} second(s)".format(duration.seconds))
            print("")

        else: 
            print(Fore.RED + "rev is not installed." + Style.RESET_ALL)
            
            finishedDateTime = datetime.now()

            print("Finished checking rev at", finishedDateTime.strftime("%m-%d-%Y %I:%M %p"))

            duration = finishedDateTime - startDateTime
            print("Total execution time: {0} second(s)".format(duration.seconds))
            exit("")
        
    except Exception: 
        print(Fore.RED + "Failed to check rev.")
        traceback.print_exc()
        exit("" + Style.RESET_ALL)


checkRev()
