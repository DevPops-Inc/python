#!/bin/python

# check htop on Mac and Linux

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


def checkHtop(): 
    print("\nCheck htop on Mac.\n")


    try:
        checkOsForMacOrLinux()

        startDateTime = datetime.now()
        print("Started checking htop at", startDateTime.strftime("%m-%d-%Y %I:%M %p"))

        FNULL = open(os.devnull,  'w')

        checkAnsibleOnMacOrLinux = subprocess.call(['which', 'htop'], stdout=FNULL) 

        if checkAnsibleOnMacOrLinux == 0:
            print(Fore.GREEN + "htop is installed."+ Style.RESET_ALL)
            os.system('htop --version')
            print(Fore.GREEN + "Successfully checked htop." + Style.RESET_ALL)

            finishedDateTime = datetime.now()

            print("Finished checking htop at", finishedDateTime.strftime("%m-%d-%Y %I:%M %p"))

            duration = finishedDateTime - startDateTime
            print("Total execution time: {0} second(s)".format(duration.seconds))
            print("")

        else: 
            raise Exception("htop is not installed.")
        
    except Exception: 
        print(Fore.RED + "Failed to check htop.")
        traceback.print_exc()
        exit("" + Style.RESET_ALL)
        

checkHtop()
