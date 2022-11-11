#!/bin/python

# check carthage on Mac

import colorama, os, sys, subprocess, traceback
from colorama import Fore, Style
from datetime import datetime
colorama.init()


def checkOsForMac():
    print("Started checking operating system at", datetime.now().strftime("%Y-%m-%d %H:%M %p"))

    if sys.platform == "darwin": 
        print(Fore.GREEN + "Operating System: ")
        os.system('sw_vers')
        print(Style.RESET_ALL, end="")
        
        print("Finished checking operating system at", datetime.now().strftime("%Y-%m-%d %H:%M %p"))

        print("")

    else: 
        print(Fore.RED + "Sorry but this script only runs on Mac." + Style.RESET_ALL)
        
        print("Finished checking operating system at", datetime.now().strftime("%Y-%m-%d %H:%M %p"))

        exit("")


def checkCarthage(): 
    print("\nCheck carthage on Mac.\n")
    checkOsForMac()

    try:
        startDateTime = datetime.now()
        
        print("Started checking carthage at", startDateTime.strftime("%Y-%m-%d %H:%M %p"))

        FNULL = open(os.devnull,'w')

        checkAnsibleOnMacOrLinux = subprocess.call(['which', 'brew'], stdout=FNULL) 

        if checkAnsibleOnMacOrLinux == 0:
            print(Fore.GREEN + "carthage is installed."+ Style.RESET_ALL)
            os.system('brew --version')
            print(Fore.GREEN + "Successfully checked carthage." + Style.RESET_ALL)

            finishedDateTime = datetime.now()

            print("Finished checking Hombrew at", finishedDateTime.strftime("%Y-%m-%d %H:%M %p"))

            duration = finishedDateTime - startDateTime
            print("Total execution time: {0} second(s)".format(duration.seconds))
            print("")

        else: 
            print(Fore.RED + "carthage is not installed." + Style.RESET_ALL)
            
            finishedDateTime = datetime.now()

            print("Finished checking carthage at", finishedDateTime.strftime("%Y-%m-%d %H:%M %p"))

            duration = finishedDateTime - startDateTime
            print("Total execution time: {0} second(s)".format(duration.seconds))
            exit("")
        
    except Exception as e: 
        print(Fore.RED + "Failed to check carthage.")
        print(e)
        print(traceback.print_stack)
        exit("" + Style.RESET_ALL)


checkCarthage()
