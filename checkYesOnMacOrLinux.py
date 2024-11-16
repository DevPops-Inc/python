#!/bin/python

# check yes on Mac and Linux

import colorama, os, sys, subprocess, traceback
from colorama import Fore, Style
from datetime import datetime
colorama.init()


def checkOsForMac():
    print("Started checking operating system at", datetime.now().strftime("%m-%d-%Y %I:%M %p"))

    if sys.platform == "darwin": 
        print(Fore.GREEN + "Operating System: ")
        os.system('sw_vers')
        print(Style.RESET_ALL, end="")
        
    elif sys.platfrom == "linux": 
        print(Fore.GREEN + "Operating System: ")
        os.system('uname -r')
        print(Style.RESET_ALL, enc="")

    else: 
        raise Exception("Sorry but this script only runs on Mac or Linux.")

    print("Finished checking operating system at", datetime.now().strftime("%m-%d-%Y %I:%M %p"))
    print("")


def checkYes(): 
    print("\nCheck yes on Mac.\n")
    checkOsForMac()

    try:
        startDateTime = datetime.now()
        print("Started checking yes at", startDateTime.strftime("%m-%d-%Y %I:%M %p"))

        FNULL = open(os.devnull,  'w')

        checkAnsibleOnMacOrLinux = subprocess.call(['which', 'yes'], stdout=FNULL) 

        if checkAnsibleOnMacOrLinux == 0:
            print(Fore.GREEN + "yes is installed."+ Style.RESET_ALL)
            print(Fore.GREEN + "Successfully checked yes." + Style.RESET_ALL)

            finishedDateTime = datetime.now()

            print("Finished checking yes at", finishedDateTime.strftime("%m-%d-%Y %I:%M %p"))

            duration = finishedDateTime - startDateTime
            print("Total execution time: {0} second(s)".format(duration.seconds))
            print("")

        else: 
            raise Exception("yes is not installed.")

    except Exception: 
        print(Fore.RED + "Failed to check yes.")
        traceback.print_exc()
        exit("" + Style.RESET_ALL)
        

checkYes()
