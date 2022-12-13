#!/bin/python

# launch YouTube in Chrome on Mac

import colorama, os, sys, subprocess, traceback
from colorama import Fore, Style
from datetime import datetime
colorama.init()


def checkOsForMac(): 
    print("Started checking operating system at", datetime.now().strftime("%m-%d-%Y %I:%M %p"))

    if sys.platform == "darwin": 
        print(Fore.GREEN + "Operating System:")
        os.system('sw_vers')
        print(Style.RESET_ALL, end="")

        print("Finished checking operating system at", datetime.now().strftime("%m-%d-%Y %I:%M %p"))
        print("")

    else:
        print(Fore.RED + "Sorry but this script only runs on Mac." + Style.RESET_ALL)

        print("Finished checking operating system at", datetime.now().strftime("%m-%d-%Y %I:%M %p"))
        exit("")


def checkChrome():
    print("Started checking Chrome at", datetime.now().strftime("%m-%d-%Y %I:%M %p"))

    chromeInApps = os.system('open -Ra "Google Chrome.app"')

    if chromeInApps == 0:
        print(Fore.GREEN + "Chrome is installed." + Style.RESET_ALL)

        print("Finished checking Chrome at", datetime.now().strftime("%m-%d-%Y %I:%M %p"))
        print("")

    else: 
        print(Fore.RED + "Chrome is not installed." + Style.RESET_ALL)

        print("Finished checking Chrome at", datetime.now().strftime("%m-%d-%Y %I:%M %p"))
        exit("")


def launchYouTubeInChrome():
    print("\nLaunch YouTube in Chrome on Mac.\n")
    
    checkOsForMac()
    checkChrome()

    try: 
        startDateTime = datetime.now()
        print("Started launching YouTube in Chrome at", startDateTime.strftime("%m-%d-%Y %I:%M %p"))

        youTubeInChrome = str(os.system('open -a "Google Chrome.app" http://youtube.com'))
        
        if os.system(youTubeInChrome) != 0: 
            raise Exception("Attempt threw an error! ") # TODO: figure out why it throws "sh: 0: command not found" error but still launches YouTube anyway

        print(Fore.GREEN + "Successfully launched YouTube in Chrome." + Style.RESET_ALL)

        finishedDateTime = datetime.now()

        print("Finished launching YouTube in Chrome at", finishedDateTime.strftime("%m-%d-%Y %I:%M %p"))

        duration = finishedDateTime - startDateTime
        print("Total execution time: {0} second(s)".format(duration.seconds))
        print("")

    except Exception as e: 
        print(Fore.RED + "Failed to launch YouTube in Chrome.")
        print(e)
        print(traceback.print_stack)
        exit("" + Style.RESET_ALL)


launchYouTubeInChrome()
