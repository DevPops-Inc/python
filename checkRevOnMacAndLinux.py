#!/bin/python

# check rev on Mac and Linux

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

def checkRev(): 
    print("\nCheck rev on Mac.\n")
    checkOsForMac()

    try:
        startDateTime = datetime.now()
        
        print("Started checking rev at", startDateTime.strftime("%Y-%m-%d %H:%M %p"))

        FNULL = open(os.devnull,'w')

        checkAnsibleOnMacOrLinux = subprocess.call(['which', 'rev'], stdout=FNULL) 

        if checkAnsibleOnMacOrLinux == 0:
            print(Fore.GREEN + "rev is installed." + Fore.BLUE)
            os.system('echo "rev is installed." | rev')
            print(Fore.GREEN + "Successfully checked rev." + Style.RESET_ALL)

            finishedDateTime = datetime.now()

            print("Finished checking rev at", finishedDateTime.strftime("%Y-%m-%d %H:%M %p"))

            duration = finishedDateTime - startDateTime
            print("Total execution time: {0} second(s)".format(duration.seconds))
            print("")

        else: 
            print(Fore.RED + "rev is not installed." + Style.RESET_ALL)
            
            finishedDateTime = datetime.now()

            print("Finished checking rev at", finishedDateTime.strftime("%Y-%m-%d %H:%M %p"))

            duration = finishedDateTime - startDateTime
            print("Total execution time: {0} second(s)".format(duration.seconds))
            exit("")
        
    except Exception as e: 
        print(Fore.RED + "Failed to check rev.")
        print(e)
        print(traceback.print_stack)
        exit("" + Style.RESET_ALL)

checkRev()