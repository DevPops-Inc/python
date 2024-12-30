#!/bin/python

# stop and relaunch Outlook on Windows or Mac 

import colorama, os, sys, time, traceback
from colorama import Fore, Style 
from datetime import datetime
from pathlib import PureWindowsPath
colorama.init()


def checkOsForWinOrMac(): 

    print("Started checking operating system at", datetime.now().strftime("%m-%d-%Y %I:%M %p"))

    if sys.platform == "win32": 
        print(Fore.GREEN + "Operating System:", end=""); sys.stdout.flush()
        os.system('ver')
        print(Style.RESET_ALL, end="")
        operatingSystem = "Windows"

    elif sys.platform == "darwin": 
        print(Fore.GREEN + "Operating System:")
        os.system('sw_vers')
        print(Style.RESET_ALL, end="")
        operatingSystem = "macOS"

    else: 
        raise Exception(Fore.RED + "Sorry but this script only runs on Windows or Mac.")

    print("Finished checking operating system at", datetime.now().strftime("%m-%d-%Y %I:%M %p"))

    print("")
    return operatingSystem


def checkOutlook(operatingSystem): 
    print("Started checking Outlook at", datetime.now().strftime("%m-%d-%Y %I:%M %p"))

    if operatingSystem == "Windows": 
        
        outlookPath = PureWindowsPath("C:/Program Files/Microsoft Office/root/Office16/OUTLOOK.EXE")

        if os.path.exists(outlookPath) == True: 
            print(Fore.GREEN + "Outlook is installed." + Style.RESET_ALL)

            print("Finished checking Outlook at", datetime.now().strftime("%m-%d-%Y %I:%M %p"))
            print("")

        else: 
            raise Exception(Fore.RED + "Outlook is not installed.")

    elif operatingSystem == "macOS": 

        bashOutlookCheck = "open -Ra 'Microsoft Outlook.app'"

        if os.system(bashOutlookCheck) == 0: 
            print(Fore.GREEN + "Outlook is installed." + Style.RESET_ALL)

            print("Finished checking Outlook at", datetime.now().strftime("%m-%d-%Y %I:%M %p"))

            print("")

        else: 
            raise Exception(Fore.RED + "Outlook is not installed.")


def stopAndRelaunchOutlook(): 
    print("\nStop and relaunch Outlook on Windows or Mac.\n")

    try: 
        operatingSystem = checkOsForWinOrMac()
        outlookPath = checkOutlook(operatingSystem)
    
        startDateTime = datetime.now()
        
        print("Started stopping and relauching Outlook at", startDateTime.strftime("%m-%d-%Y %I:%M %p"))

        if operatingSystem == "Windows": 
            outlookApp = 'outlook.exe'
            stopOutlook = 'taskkill /F /IM {0}'.format(outlookApp)

            outlookPath = PureWindowsPath("C:/Program Files/Microsoft Office/root/Office16/OUTLOOK.EXE")

            launchOutlook = 'explorer {0}'.format(outlookPath)

            if os.system(stopOutlook) == 0: 

                print(Fore.BLUE + "Stopped Outlook and relaunching in 5 seconds.")
                time.sleep(5)

            os.system(launchOutlook)

        elif operatingSystem == "macOS": 
            stopOutlook = 'pkill "Microsoft Outlook"'
            launchOutlook = 'open -a "Microsoft Outlook.app"'

            if os.system(stopOutlook) == 0: 

                print(Fore.BLUE + "Stopped Outlook and relaunching in 5 seconds.")
                time.sleep(5)

            if os.system(launchOutlook) != 0:
                raise Exception("Error occurred while relaunching Outlook.")
            
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
