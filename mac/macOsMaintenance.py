#!/bin/python 

# macOS maintenance 

import colorama, os, sys, traceback
from colorama import Fore, Style
from datetime import datetime
colorama.init()


def checkOsForMac():
    print("Started checking operating system at ", datetime.now().strftime("%m-%d-%Y %I:%M %p"))

    if sys.platform == "darwin":
        print(Fore.GREEN + "Operating System:")
        os.system('sw_vers')
        print(Style.RESET_ALL, end="")
        
        print("Finished checking operating system at ", datetime.now().strftime("%m-%d-%Y %I:%M %p"))
        print("")

    else: 
        raise Exception("Sorry but this script only works on Mac")


def runMacMaintenance():
    print("\nRun Mac maintenance.\n")
    checkOsForMac()

    try: 
        startDateTime = datetime.now()
        print("Started running Mac maintenance at ", startDateTime.strftime("%m-%d-%Y %I:%M %p"))

        checkMacOs = 'diskutil list | grep "MacOS"'
        checkMacintoshHd = 'diskutil list | grep "Macintosh HD"'

        if os.system(checkMacOs) == 0: 
            print(Fore.BLUE + "Disk name is MacOS.")
            hdd = "MacOS"

        elif os.system(checkMacintoshHd) == 0: 
            print(Fore.BLUE + "Disk name is Macintosh HD.")
            hdd = "Macintosh HD"

        else: 
            raise Exception("Disk name isn't MacOS or Macintosh HD.")
        
        verifyVolume = 'distutil verifyVolume "{0}"'.format(hdd)
        
        maintenance = ['sudo mdutil -i on /', 'softwareupdate --install --all', verifyVolume ]

        for jobs in maintenance: 
            if os.system(jobs) != 0: 
                raise Exception("Error occurred while performing Mac mainteance.")

        print(Fore.GREEN + "Successfully ran Mac maintenance." + Style.RESET_ALL)

        finishedDateTime = datetime.now()

        print("Finished running Mac maintenance at ", finishedDateTime.strftime("%m-%d-%Y %I:%M %p"))

        duration = finishedDateTime - startDateTime
        print("Total execution time: {0} second(s)".format(duration.seconds))
        print("")

        print("Please save your documents and close applications.")
        str(input("Press any key to restart Mac."))

        if os.system('reboot') != 0: 
            raise Exception("Error occurred while restarting computer.")
        
    except Exception: 
        print(Fore.RED + "Failed to run Mac maintenance.")
        traceback.print_exc()
        exit("" + Style.RESET_ALL)
        

runMacMaintenance()
