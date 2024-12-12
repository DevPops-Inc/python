#!/bin/python 

# check Outlook on Mac 

import colorama, os, sys, traceback
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
        raise Exception("Sorry but this script only runs on Mac.")


def checkOutlook():
    print("\nCheck Outlook on Mac.\n")
    checkOsForMac()

    try: 
        startDateTime = datetime.now()
        print("Started checking Outlook at", startDateTime.strftime("%m-%d-%Y %I:%M %p"))

        bashOutlookCheck = "open -Ra 'Microsoft Outlook.app'"

        if os.system(bashOutlookCheck) == 0: 
            print(Fore.GREEN + "Outlook is installed." + Style.RESET_ALL)

            finishedDateTime = datetime.now()
            print("Finished checking Outlook at", finishedDateTime.strftime("%m-%d-%Y %I:%M %p"))

            duration = finishedDateTime - startDateTime
            print("Total execution time: {0} second(s)".format(duration.seconds))
            print("")

        else: 
            print(Fore.RED + "Outlook is not installed." + Style.RESET_ALL)

            finishedDateTime = datetime.now()
            print("Finished checking Outlook at", finishedDateTime.strftime("%m-%d-%Y %I:%M %p"))

            duration = finishedDateTime - startDateTime
            print("Total execution time: {0} second(s)".format(duration.seconds))
            exit("")

    except Exception: 
        print(Fore.RED + "Failed to check Outlook.")
        traceback.print_exc()
        exit("" + Style.RESET_ALL)


checkOutlook()
