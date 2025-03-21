#!/bin/python

# get hard drive info on Windows

import colorama, os, sys, traceback
from colorama import Fore, Style
from datetime import datetime
colorama.init()


def checkOsForWindows():
    print("Start checking operating system at", datetime.now().strftime("%m-%d-%Y %I:%M %p"))

    if sys.platform == "win32": 
        print(Fore.GREEN + "Operating System:", end=""); sys.stdout.flush()
        os.system('ver')
        print(Style.RESET_ALL, end="")
        
        print("Finished checking operating system at", datetime.now().strftime("%m-%d-%Y %I:%M %p"))

        print("")

    else: 
        raise Exception("Sorry but this script only runs on Windows.")


def getHardDriveInfo():
    print("\nGet Hard Drive Info on Windows.\n")

    try: 
        checkOsForWindows()
        
        startDateTime = datetime.now()
        
        print("Started getting hard drive info at", startDateTime.strftime("%m-%d-%Y %I:%M %p"))

        if os.system('PowerShell "Get-PhysicalDisk | Format-Table -AutoSize"') != 0: 
            raise Exception("Error occurred while getting hard drive info.")
        
        print(Fore.GREEN + "Successfully got hard drive info." + Style.RESET_ALL)

        finishedDateTime = datetime.now()

        print("Finished getting hard drive info at", finishedDateTime.strftime("%m-%d-%Y %I:%M %p"))

        duration = finishedDateTime - startDateTime
        print("Total execution time: {0} second(s)".format(duration.seconds))
        print("")
        
    except Exception: 
        print(Fore.RED + "Failed to get hard drive info.")
        traceback.print_exc()
        exit("" + Style.RESET_ALL)
        

getHardDriveInfo()
