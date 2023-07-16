#!/bin/python

# defrag hard drive on Windows

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
        
        print("Finished checking operating system at ", datetime.now().strftime("%m-%d-%Y %I:%M %p"))

        print("")
    else: 
        print(Fore.RED + "Sorry but this script only runs on Windows." + Style.RESET_ALL)

        print("Finished checking operating system at", datetime.now().strftime("%m-%d-%Y %I:%M %p"))

        exit("")


def defragHardDrive():
    print("\nDefrag Hard Drive on Windows.\n")
    checkOsForWindows()

    try: 
        startDateTime = datetime.now()
        print("Started checking hard drive at", startDateTime.strftime("%m-%d-%Y %I:%M %p"))

        diskType = os.popen('PowerShell "Get-PhysicalDisk').read()
        print(diskType, end="")

        if "HDD" in diskType: 
            print(Fore.GREEN + "Successfully defragged hard drive ." + Style.RESET_ALL)
            
            if os.system('defrag c: /u') != 0:
                raise Exception("Couldn't defrag hard drive.")
        else: 
            print(Fore.GREEN + "Hard drive doesn't need to be defragged." + Style.RESET_ALL)

        finishedDateTime = datetime.now()
        
        print("Finished checking hard drive at", finishedDateTime.strftime("%m-%d-%Y %I:%M %p"))

        duration = finishedDateTime - startDateTime
        print("Total execution time: {0} second(s)".format(duration.seconds))
        print("")
    except Exception: 
        print(Fore.RED + "Failed to defrag hard drive.")
        
        traceback.print_exc()
        exit("" + Style.RESET_ALL)


defragHardDrive()
