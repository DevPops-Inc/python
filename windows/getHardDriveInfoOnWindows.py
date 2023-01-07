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
        print(Fore.RED + "Sorry but this script only runs on Windows." + Style.RESET_ALL)

        print("Finished checking operating system at", datetime.now().strftime("%m-%d-%Y %I:%M %p"))

        exit("")


def getHardDriveInfo():
    print("\nGet Hard Drive Info on Windows.\n")
    checkOsForWindows()

    try: 
        startDateTime = datetime.now()
        print("Started getting hard drive info at", startDateTime.strftime("%m-%d-%Y %I:%M %p"))

        os.system('PowerShell "Get-PhysicalDisk | Format-Table -AutoSize"')
        print(Fore.GREEN + "Successfully got hard drive info." + Style.RESET_ALL)

        finishedDateTime = datetime.now()

        print("Finished getting hard drive info at", finishedDateTime.strftime("%m-%d-%Y %I:%M %p"))

        duration = finishedDateTime - startDateTime
        print("Total execution time: {0} second(s)".format(duration.seconds))
        print("")
        
    except Exception as e: 
        print(Fore.RED + "Failed to get hard drive info.")
        print(e)
        print(traceback.print_stack)
        exit("" + Style.RESET_ALL)
        

getHardDriveInfo()
