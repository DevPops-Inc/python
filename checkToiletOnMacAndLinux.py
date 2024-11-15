#!/bin/python

# check TOIlet on Mac and Linux

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
        raise Exception("Sorry but this only runs on Mac or Linux.")
    
    print("Finished checking operating system at", datetime.now().strftime("%m-%d-%Y %I:%M %p"))
    print("")


def checkToilet(): 
    print("\nCheck TOIlet on Mac.\n")
    checkOsForMacOrLinux()

    try:
        startDateTime = datetime.now()
        print("Started checking TOIlet at", startDateTime.strftime("%m-%d-%Y %I:%M %p"))

        FNULL = open(os.devnull,  'w')

        checkAnsibleOnMacOrLinux = subprocess.call(['which', 'toilet'], stdout=FNULL) 

        if checkAnsibleOnMacOrLinux == 0:
            print(Fore.GREEN + "TOIlet is installed."+ Style.RESET_ALL)
            os.system('toilet --version')
            print(Fore.GREEN + "Successfully checked TOIlet." + Style.RESET_ALL)

            finishedDateTime = datetime.now()

            print("Finished checking TOIlet at", finishedDateTime.strftime("%m-%d-%Y %I:%M %p"))

            duration = finishedDateTime - startDateTime
            print("Total execution time: {0} second(s)".format(duration.seconds))
            print("")

        else: 
            raise Exception("TOIlet is not installed.")
        
    except Exception: 
        print(Fore.RED + "Failed to check TOIlet.")
        traceback.print_exc()
        exit("" + Style.RESET_ALL)


checkToilet()
