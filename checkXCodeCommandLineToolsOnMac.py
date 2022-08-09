#!/bin/python

# check XCode command line tools on Mac

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
        
        print("Finished checking operating system at", datetime.now().strftime("%Y-%m-%d %H:%M %p"))

        print("")

    else: 
        print(Fore.RED + "Sorry but this script only runs on Mac." + Style.RESET_ALL)
        
        print("Finished checking operating system at", datetime.now().strftime("%Y-%m-%d %H:%M %p"))

        exit("")

def checkXCodeCommandLineTools(): 
    print("\nCheck XCode command line tools on Mac.\n")
    checkOsForMac()

    try:
        startDateTime = datetime.now()
        
        print("Started checking XCode command line tools at", startDateTime.strftime("%Y-%m-%d %H:%M %p"))

        FNULL = open(os.devnull,'w')

        checkAnsibleOnMacOrLinux = subprocess.call(['which', 'xcode-select'], stdout=FNULL) 

        if checkAnsibleOnMacOrLinux == 0:
            print(Fore.GREEN + "XCode command line tools are installed."+ Style.RESET_ALL)
            os.system('xcode-select --version')
            print(Fore.GREEN + "Successfully checked XCode command line tools." + Style.RESET_ALL)

            finishedDateTime = datetime.now()

            print("Finished checking XCode command line tools at", finishedDateTime.strftime("%Y-%m-%d %H:%M %p"))

            duration = finishedDateTime - startDateTime
            print("Total execution time: {0} second(s)".format(duration.seconds))
            print("")

        else: 
            print(Fore.RED + "XCode command line tools are not installed." + Style.RESET_ALL)
            
            finishedDateTime = datetime.now()

            print("Finished checking XCode command line tools at", finishedDateTime.strftime("%Y-%m-%d %H:%M %p"))

            duration = finishedDateTime - startDateTime
            print("Total execution time: {0} second(s)".format(duration.seconds))
            exit("")
        
    except Exception as e: 
        print(Fore.RED + "Failed to check XCode command line tools.")
        print(e)
        print(traceback.print_stack)
        exit("" + Style.RESET_ALL)

checkXCodeCommandLineTools()
