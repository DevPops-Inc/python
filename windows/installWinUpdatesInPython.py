#!/bin/python

# install Windows updates in Python

# run this script as administrator

import colorama, os, sys, traceback
from colorama import Fore, Style
from datetime import datetime
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
        raise Exception("Sorry but this script only runs on Windows.")


def installWindowsUpdates():
    print("\nInstall Windows updates in Python.\n")
    checkOsForWindows()

    try:
        startDateTime = datetime.now()
        
        print("Started installing Windows updates at", startDateTime.strftime("%m-%d-%Y %I:%M %p"))

        windowsUpates = ['Powershell "Install-Module PSWindowsUpdate -Force"', 'PowerShell "Get-WindowsUpdate -AcceptAll -Install"'] 

        for update in windowsUpates:
            if os.system(update) != 0: 
                raise Exception("Error occurred while installing Windows updates.")

        print(Fore.GREEN + "Successfully installed Windows updates." + Style.RESET_ALL)

        finishedDateTime = datetime.now()

        print("Finished installing Windows updates at", finishedDateTime.strftime("%m-%d-%Y %I:%M %p"))

        duration = finishedDateTime - startDateTime
        print("Total execution time: {0} second(s)".format(duration.seconds))
        print("")
        
        print(Fore.BLUE + "Please save your work and close applications.")
        input("Press any key to restart computer.")
        os.system('shutdown /r /t 0')

    except Exception as e:
        print(Fore.RED + "Failed to install Windows updates.")
        traceback.print_exc()
        exit("" + Style.RESET_ALL)


installWindowsUpdates()
