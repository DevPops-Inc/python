#!/bin/python 

# check Android Studio on Mac

import colorama, os, sys, traceback
from colorama import Fore, Style
from datetime import datetime
colorama.init()


def checkOsForMac():
    print("Started checking operating system at", datetime.now().strftime("%m-%d-%Y %H:%M %p"))

    if sys.platform == "darwin": 
        print(Fore.GREEN + "Operating System: ")
        os.system('sw_vers')
        print(Style.RESET_ALL, end="")

        print("Finished checking operating system at", datetime.now().strftime("%m-%d-%Y %I:%M %p"))
        
        print("")
        
    else: 
        raise Exception("Sorry this script only runs on macOS.")


def getDesktopApp(): 
    
    desktopApp = str(input("Please type the desktop application and press the \"return\" key (Example: Android Studio): "))

    print("")
    return desktopApp
        

def checkParameters(desktopApp): 
    print("Started checking parameter(s) at", datetime.now().strftime("%m-%d-%Y %I:%M %p"))
    valid = True

    print("Parameter(s): ")
    print("----------------------------------")
    print("desktopApp: {0}".format(desktopApp))
    print("----------------------------------")

    if desktopApp == None or desktopApp == "": 
        print(Fore.RED + "desktopApp is not set." + Style.RESET_ALL)
        valid = False

    if valid == True: 
        print(Fore.GREEN + "All parameter check(s) passed." + Style.RESET_ALL)

        print("Finished checking parameter(s) at", datetime.now().strftime("%m-%d-%Y %I:%M %p"))
        print("")

    else: 
        raise Exception("One or more parameters are incorrect.")


def checkAndroidStudio():
    print("\nCheck Android Studio on Mac.\n")
    checkOsForMac()

    desktopApp = "Android Studio"

    if desktopApp == None or desktopApp == "": 
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
            

    except Exception: 
        print(Fore.RED + "Failed to check Android Studio.")
        traceback.print_exc()
        exit("" + Style.RESET_ALL)


checkAndroidStudio()
