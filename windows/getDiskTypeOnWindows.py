#!/bin/python 

# get disk type on Windows

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
        print(Fore.RED + "Sorry but this script only runs on Windows." + Style.RESET_ALL)

        print("Finished checking operating system at", datetime.now().strftime("%m-%d-%Y %I:%M %p"))

        exit("")


def getDiskType(): 
    print("\nGet disk type on Windows.\n")
    checkOsForWindows()

    try: 
        startDateTime = datetime.now()
        print("Started getting disk type at", startDateTime.strftime("%m-%d-%Y %I:%M %p"))

        diskType = os.popen('PowerShell "Get-PhysicalDisk').read()
        print(diskType, end="")

        if "SSD" in diskType: 
            print(Fore.BLUE + "Disk type is SSD.")
            
        elif "HDD" in diskType: 
            print(Fore.BLUE + "Disk type is HDD.")

        else: 
            raise Exception("Error occurred while getting disk type.")

        print(Fore.GREEN + "Successfully got disk type." + Style.RESET_ALL)

        finishedDateTime = datetime.now()
        print("Finished getting disk type at", finishedDateTime.strftime("%m-%d-%Y %I:%M %p"))

        duration = finishedDateTime - startDateTime
        print("Total execution time: {0} second(s)".format(duration.seconds))
        print("")

    except Exception: 
        print(Fore.RED + "Failed to get disk type.")
        traceback.print_exc()
        exit("" + Style.RESET_ALL)


getDiskType()
