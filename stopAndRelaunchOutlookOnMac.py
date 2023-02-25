#!/bin/python

# stop and relaunch Outlook on Mac 

import colorama, os, sys, time, traceback
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


def checkOutlook(): 
    print("Started checking Outlook at", datetime.now().strftime("%m-%d-%Y %I:%M %p"))

    bashOutlookCheck = "open -Ra 'Microsoft Outlook.app'"

    if os.system(bashOutlookCheck) == 0: 
        print(Fore.GREEN + "Outlook is installed." + Style.RESET_ALL)

        print("Finished checking Outlook at", datetime.now().strftime("%m-%d-%Y %I:%M %p"))
        print("")

    else: 
        print(Fore.RED + "Outlook is not installed." + Style.RESET_ALL)

        print("Finished checking Outlook at", datetime.now().strftime("%m-%d-%Y %I:%M %p"))
        exit("")


def stopAndRelaunchOutlook(): 
    print("\nStop and relaunch Outlook on Mac.\n")
    
    checkOsForMac()
    checkOutlook()

    stopOutlook = 'pkill "Microsoft Outlook"'
    launchOutlook = 'open -a "Microsoft Outlook.app"'

    try: 
        startDateTime = datetime.now()
        
        print("Started stopping and relauching Outlook at", startDateTime.strftime("%m-%d-%Y %I:%M %p"))

        if os.system(stopOutlook) == 0: 
            print(Fore.BLUE + "Stopped Outlook and relaunching in 5 seconds.")
            time.sleep(5)

        if os.system(launchOutlook) != 0:
            raise Exception("Couldn't relaunch Outlook!")
            
        print(Fore.GREEN + "Successfully stopped and relaunched Outlook." + Style.RESET_ALL)

        finishedDateTime = datetime.now()

        print("Finished stopping and relaunching Outlook at", finishedDateTime.strftime("%m-%d-%Y %I:%M %p"))

        duration = finishedDateTime - startDateTime
        print("Total execution time: {0} second(s)".format(duration.seconds))
        print("")

    except Exception: 
        print(Fore.RED + "Failed to stop and relaunch Outlook.")
        traceback.print_exc()
        exit("" + Style.RESET_ALL)


stopAndRelaunchOutlook()
