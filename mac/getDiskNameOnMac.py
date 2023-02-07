#!/bin/python 

# get disk name on Mac

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
        print(Fore.RED + "Sorry but this script only runs on Mac." + Style.RESET_ALL)

        print("Finished checking operating system at", datetime.now().strftime("%m-%d-%Y %I:%M %p"))
        exit("")


def getDiskName(): 
    print("\nGet disk name on Mac.\n")
    checkOsForMac()

    try: 
        startDateTime = datetime.now()
        print("Started getting disk name at", startDateTime.strftime("%m-%d-%Y %I:%M %p"))

        checkMacOs = 'diskutil list | grep "MacOS"'
        checkMacintoshHd = 'diskutil list | grep "Macintosh HD"'

        if os.system(checkMacOs) == 0: 
            print(Fore.BLUE + "Disk name is MacOS.")

        elif os.system(checkMacintoshHd) == 0: 
            print(Fore.BLUE + "Disk name is Macintosh HD.")

        else: 
            raise Exception("Disk name isn't MacOS or Macintosh HD.")

        print(Fore.GREEN + "Successfully got disk name." + Style.RESET_ALL)

        finisheDateTime = datetime.now()
        print("Finished getting disk name at", finisheDateTime.strftime("%m-%d-%Y %I:%M %p"))

        duration = finisheDateTime - startDateTime
        print("Total execution time: {0} second(s)".format(duration.seconds))
        print("")

    except Exception: 
        print(Fore.RED + "Failed to get disk name.")
        traceback.print_exc()
        exit("" + Style.RESET_ALL)


getDiskName()
