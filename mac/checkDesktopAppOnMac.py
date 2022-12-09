#!/bin/python 

# check desktop application on Mac

# you can run this script with: python3 checkDesktopAppOnMac.py "< desktop application >""

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

        print("Finished checking operating system at", datetime.now().strftime("%m-%d-%Y %I:%M %p"))
        print("")
    else: 
        print(Fore.RED + "Sorry this script only runs on macOS." + Style.RESET_ALL)

        print("Finished checking operating system at", datetime.now().strftime("%m-%d-%Y %I:%M %p"))
        exit("")

        
def getDesktopApp(): 
    desktopApp = str(input("Please type the desktop application and press the \"return\" key (Example: Google Chrome.app): "))

    print("")
    return desktopApp
        

def checkParameters(desktopApp): 
    print("Started checking parameter(s) at", datetime.now().strftime("%m-%d-%Y %I:%M %p"))
    valid = "true"

    print("Parameter(s): ")
    print("----------------------------------")
    print("desktopApp: {0}".format(desktopApp))
    print("----------------------------------")

    if desktopApp == None: 
        print(Fore.RED + "desktopApp is not set." + Style.RESET_ALL)
        valid = "false"

    if valid == "true": 
        print(Fore.GREEN + "All parameter check(s) passed." + Style.RESET_ALL)

        print("Finished checking parameter(s) at", datetime.now().strftime("%m-%d-%Y %I:%M %p"))
        print("")

    else: 
        print(Fore.RED + "One or more parameters are incorrect." + Style.RESET_ALL)

        print("Finished checking parameter(s) at", datetime.now().strftime("%m-%d-%Y %I:%M %p"))
        exit("")


def checkDesktopApp():
    print("\nCheck desktop application on Mac.\n")
    checkOsForMac()

    if len(sys.argv) >= 2: 
        desktopApp = str(sys.argv[1])

    else: 
        desktopApp = getDesktopApp()

    checkParameters(desktopApp)

    try: 
        startDateTime = datetime.now()

        print("Started checking {0} at {1}".format(desktopApp, startDateTime.strftime("%m-%d-%Y %I:%M %p")))

        bashDesktopAppCheck = "open -Ra '{0}'".format(desktopApp)
        desktopAppInApps = os.system(bashDesktopAppCheck)

        if desktopAppInApps == 0:
            print(Fore.GREEN + "{0} is installed.".format(desktopApp) + Style.RESET_ALL)

            finishedDateTime = datetime.now()

            print("Finished checking {0} at {1}".format(desktopApp, finishedDateTime.strftime("%m-%d-%Y %I:%M %p")))

            duration = finishedDateTime - startDateTime
            print("Total execution time: {0} second(s)".format(duration.seconds))
            print("")

        else: 
            print(Fore.RED + "{0} is not installed.".format(desktopApp) + Style.RESET_ALL)

            finishedDateTime = datetime.now()
            print("Finished checking {0} at {1}".format(desktopApp, finishedDateTime.strftime("%m-%d-%Y %I:%M %p")))

            duration = finishedDateTime - startDateTime
            print("Total execution time: {0} second(s)".format(duration.seconds))
            exit("")
            
    except Exception as e: 
        print(Fore.RED + "Failed to check desktop application.")
        print(e)
        print(traceback.print_stack)
        exit("" + Style.RESET_ALL)


checkDesktopApp()
