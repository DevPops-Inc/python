#!/bin/python 

# check Chrome on Mac

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

        
def checkChrome():
    print("\nCheck Chrome on Mac.\n")
    checkOsForMac()

    try: 
        startDateTime = datetime.now()
        print("Started checking Chrome at", startDateTime.strftime("%Y-%m-%d %H:%m %p"))

        chromeInApps = os.system('open -Ra "Google Chrome.app"')

        if chromeInApps == 0:
            print(Fore.GREEN + "Chrome is installed." + Style.RESET_ALL)

            finishedDateTime = datetime.now()
            print("Finished checking Chrome at", finishedDateTime.strftime("%Y-%m-%d %H:%M %p"))

            duration = finishedDateTime - startDateTime
            print("Total execution time: {0} second(s)".format(duration.seconds))
            print("")

        else: 
            print(Fore.RED + "Chrome is not installed." + Style.RESET_ALL)

            finishedDateTime = datetime.now()
            print("Finished checking Chrome at", finishedDateTime.strftime("%Y-%m-%d %H:%M %p"))

            duration = finishedDateTime - startDateTime
            print("Total execution time: {0} second(s)".format(duration.seconds))
            exit("")
            
    except Exception as e: 
        print(Fore.RED + "Failed to check Chrome.")
        print(e)
        print(traceback.print_stack)
        exit("" + Style.RESET_ALL)


checkChrome()
