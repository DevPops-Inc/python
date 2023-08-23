#!/bin/python

# stop and relaunch Outlook on Windows 

import colorama, os, sys, time, traceback
from colorama import Fore, Style 
from datetime import datetime
from pathlib import PureWindowsPath
colorama.init()


def checkOsForWindows(): 
    print("Started checking operating system at", datetime.now().strftime("%m-%d-%Y %I:%M %p"))

    if sys.platform == "win32": 
        print(Fore.GREEN + "Operating System:", end=""); sys.stdout.flush()
        os.system('ver')
        print(Style.RESET_ALL, end="")

        print("Finished checking operating system at", datetime.now().strftime("%m-%d-%Y %I:%M %p"))

        print("")

    else: 
        print(Fore.RED + "Sorry but this script only runs on Windows." + Style.RESET_ALL)

        print("Finished checking operating system at", datetime.now().strftime("%m-%d-%Y %I:%M %p"))

        exit("")


def checkOutlook(): 
    print("Started checking Outlook at", datetime.now().strftime("%m-%d-%Y %I:%M %p"))

    outlookPath = PureWindowsPath("C:/Program Files/Microsoft Office/root/Office16/OUTLOOK.EXE")

    if os.path.exists(outlookPath) == True: 
        print(Fore.GREEN + "Outlook is installed." + Style.RESET_ALL)

        print("Finished checking Outlook at", datetime.now().strftime("%m-%d-%Y %I:%M %p"))
        print("")

    else: 
        print(Fore.RED + "Outlook is not installed." + Style.RESET_ALL)

        print("Finished checking Outlook at", datetime.now().strftime("%m-%d-%Y %I:%M %p"))
        exit("")


def stopAndRelaunchOutlook(): 
    print("\nStop and relaunch Outlook on Windows.\n")
    
    checkOsForWindows()
    checkOutlook()

    outlookApp = 'outlook.exe'
    stopOutlook = 'taskkill /F /IM {0}'.format(outlookApp)
    outlookPath = PureWindowsPath("C:/Program Files/Microsoft Office/root/Office16/OUTLOOK.EXE")
    launchOutlook = 'explorer {0}'.format(outlookPath)

    try: 
        startDateTime = datetime.now()
        
        print("Started stopping and relauching Outlook at", startDateTime.strftime("%m-%d-%Y %I:%M %p"))

        if os.system(stopOutlook) == 0: 
            print(Fore.BLUE + "Stopped Outlook and relaunching in 5 seconds.")
            time.sleep(5)
        else:
            raise Exception("Error occurred while stopping Outlook.")

        os.system(launchOutlook)
            
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
