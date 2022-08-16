#!/bin/python

# check htop on Mac and Linux

import colorama, os, sys, subprocess, traceback
from colorama import Fore, Style
from datetime import datetime
colorama.init()

def checkOsForMac():
    print("Started checking operating system at", datetime.now().strftime("%Y-%m-"))

    if sys.platform == "darwin": 
        print(Fore.GREEN + "Operating System: ")
        print(os.system('sw_vers'))
        print(Style.RESET_ALL)
        
    elif sys.platfrom == "linux": 
        print(Fore.GREEN + "Operating System: ")
        print(os.system('uname -r'))
        print(Style.RESET_ALL)

    else: 
        print(Fore.RED + "Sorry but this script only runs on Mac." + Style.RESET_ALL)
        
        print("Finished checking operating system at", datetime.now().strftime("%Y-%m-%d %H:%M %p"))

        exit("")

    print("Finished checking operating system at", datetime.now().strftime("%Y-%m-%d %H:%M %p"))

    print("")

def checkHtop(): 
    print("\nCheck htop on Mac.\n")
    checkOsForMac()

    try:
        startDateTime = datetime.now()
        
        print("Started checking htop at", startDateTime.strftime("%Y-%m-%d %H:%M %p"))

        FNULL = open(os.devnull,'w')

        checkAnsibleOnMacOrLinux = subprocess.call(['which', 'htop'], stdout=FNULL) 

        if checkAnsibleOnMacOrLinux == 0:
            print(Fore.GREEN + "htop is installed."+ Style.RESET_ALL)
            os.system('htop --version')
            print(Fore.GREEN + "Successfully checked htop." + Style.RESET_ALL)

            finishedDateTime = datetime.now()

            print("Finished checking htop at", finishedDateTime.strftime("%Y-%m-%d %H:%M %p"))

            duration = finishedDateTime - startDateTime
            print("Total execution time: {0} second(s)".format(duration.seconds))
            print("")

        else: 
            print(Fore.RED + "htop is not installed." + Style.RESET_ALL)
            
            finishedDateTime = datetime.now()

            print("Finished checking htop at", finishedDateTime.strftime("%Y-%m-%d %H:%M %p"))

            duration = finishedDateTime - startDateTime
            print("Total execution time: {0} second(s)".format(duration.seconds))
            exit("")
        
    except Exception as e: 
        print(Fore.RED + "Failed to check htop.")
        print(e)
        print(traceback.print_stack)
        exit("" + Style.RESET_ALL)

checkHtop()
