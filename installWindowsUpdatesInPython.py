#!/bin/python

# install Windows updates in Python

# run this script as administrator

import colorama, os, sys, traceback
from colorama import Fore, Style
from datetime import datetime
colorama.init()

def checkOsForWindows(): 
    print("Started checking operating system at", datetime.now().strftime("%Y-%m-%d %H:%M %p"))

    if sys.platform == "win32": 
        print(Fore.GREEN + "Operating System: ")
        print(os.system('ver'))
        print(Style.RESET_ALL)

        print("Finished checking operating system at", datetime.now().strftime("%Y-%m-%d %H:%M %p"))

        print("")
    else: 
        print(Fore.RED + "Sorry but this script only runs on Windows." + Style.RESET_ALL)

        print("Finished checking operating system at", datetime.now().strftime("%Y-%m-%d %H:%M %p"))

        exit("")

def installWindowsUpdates():
    print("\nInstall Windows updates in Python.\n")
    checkOsForWindows()

    try:
        startDateTime = datetime.now()
        
        print("Started installing Windows updates at", startDateTime.strftime("%Y-%m-%d %H:%M %p"))

        print(Fore.BLUE + "Please save your work and close your applications since the computer will restart after updates are installed.")
        
        windowsUpates = ['Powershell "Install-Module PSWindowsUpdate -Force"', 'PowerShell "Get-WindowsUpdate -AcceptAll -Install -AutoReboot"'] 

        for update in windowsUpates:
            os.system(update)

        print(Fore.GREEN + "Successfully installed Windows updates." + Style.RESET_ALL)

        finishedDateTime = datetime.now()

        print("Finished installing Windows updates at", finishedDateTime.strftime("%Y-%m-%d %H:%M %p"))

        duration = finishedDateTime - startDateTime
        print("Total execution time: {0} second(s)".format(duration.seconds))
        print("")
    except Exception as e:
        print(Fore.RED + "Failed to install Windows updates.")
        print(e)
        print(traceback.print_stack)
        exit("" + Style.RESET_ALL)

installWindowsUpdates()
