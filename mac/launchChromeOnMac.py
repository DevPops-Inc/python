#!/bin/python

# launch Chrome on Mac

import colorama, os, sys, traceback
from colorama import Fore, Style
from datetime import datetime
colorama.init()


def checkOsForMac():
    print("Started checking operating system at", datetime.now().strftime("%%m-%d-%Y I:%M %p"))

    if sys.platform == "darwin": 
        print(Fore.GREEN + "Operating System: ")
        os.system('sw_vers')
        print(Style.RESET_ALL, end="")

        print("Finished checking operating system at", datetime.now().strftime("%Y-%m-%d %H:%M %p"))
        print("")
    else: 
        print(Fore.RED + "Sorry this script only runs on macOS." + Style.RESET_ALL)

        print("Finished checking operating system at", datetime.now().strftime("%Y-%m-%d %H:%M %p"))
        exit("")


def launchChrome(): 
    print("\nLaunch Chrome on Mac\n")
    operatingSystem = checkOsForMac()

    try: 
        startDateTime = datetime.now()
        print("Started launching Chrome at", startDateTime.strftime("%Y-%m-%d %H:%M %p"))

        browser=os.system('open -a "Google Chrome"')
        print(Fore.GREEN + "Successfully launched Chrome." + Style.RESET_ALL)

        finishedDateTime = datetime.now()
        print("Finished launching Chrome at", finishedDateTime.strftime("%Y-%m-%d %H:%M %p"))

        duration = finishedDateTime - startDateTime
        print("Total execution time: {0} second(s)".format(duration.seconds))
        print("")
        
    except Exception as e: 
        print(Fore.RED + "Failed to launch Chrome.")
        print(e)
        print(traceback.print_stack)
        exit("" + Style.RESET_ALL)
        

launchChrome()
