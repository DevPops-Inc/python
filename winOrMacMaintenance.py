#!/bin/python

# Windows or Mac maintenance

# run this script as admin on Windows

import colorama, os, sys, traceback
from colorama import Fore, Style 
from datetime import datetime
colorama.init()


def checkOs():

    print("Started checking operating system at ", datetime.now().strftime("%m-%d-%Y %I:%M %p"))

    if sys.platform == "win32": 
        print(Fore.GREEN + "Operating System:", end=""); sys.stdout.flush()
        os.system('ver')
        print(Style.RESET_ALL, end="")
        operatingSystem = "Windows"

    elif sys.platform == "darwin": 
        print(Fore.GREEN + "Operating System: ")
        os.system('sw_vers')
        print(Style.RESET_ALL, end="")
        operatingSystem = "macOS"

    else: 
        raise Exception("Sorry but this script only runs on Windows or macOS.")

    print("Finished checking operating system at ", datetime.now().strftime("%m-%d-%Y %I:%M %p"))

    print("")
    return operatingSystem
    

def runWindowsMaintenance():
    startDateTime = datetime.now()
    
    print("Started running Windows maintenance at ", startDateTime.strftime("%m-%d-%Y %I:%M %p"))

    os.system('echo y | chkdsk /f/r c:')
        
    maintenance = ['SFC /scannow', 'Dism /Online /Cleanup-Image /ScanHealth']

    for job in maintenance: 
        if os.system(job) != 0: 
            raise Exception("Error occurred while running Windows maintenance.")

    diskType = os.popen('PowerShell "Get-PhysicalDisk').read()
    print(diskType)

    if "HDD" in diskType: 
        if os.system('defrag c: /u') != 0: 
            raise Exception("Error occurred while defragging the disk.")

    print(Fore.GREEN + "Successfully ran maintenance on Windows." + Style.RESET_ALL)

    finishedDateTime = datetime.now()

    print("Finished running Windows maintenance at ", finishedDateTime.strftime("%m-%d-%Y %I:%M %p"))

    duration = finishedDateTime - startDateTime 
    print("Total execution time: {0} second(s)".format(duration.seconds))
    print("")
    
    print("Please save your work and close applications.")
    str(input("Press any key to continue."))

    if os.system('shutdown /r /t 0') != 0:
            raise Exception("Error occurred while restarting computer.")


def runMacMaintenance():
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
    
    verifyVolume = 'diskutil verifyVolume "{0}"'.format(hdd)
    
    maintenance = ['sudo mdutil -i on /', 'softwareupdate --install --all', verifyVolume ]

    for jobs in maintenance: 
        if os.system(jobs) != 0: 
            raise Exception("Error occurred while running Mac maintenance.")

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


def computerMaintenance():
    print("\nRun computer maintenance.\n")

    try: 
        operatingSystem = checkOs()

        startDateTime = datetime.now()

        print("Started mainteance at {0}".format(startDateTime.strftime("%m-%d-%Y %I:%M %p")))

        if operatingSystem == "Windows": 
            runWindowsMaintenance()           
        elif operatingSystem == "macOS":
            runMacMaintenance()

        print(Fore.GREEN + "Successfully performed maintenance." + Style.RESET_ALL)

        finishedDateTime = datetime.now()

        print("Finished maintenance at {0}".format(finishedDateTime.strftime("%m-%d-%Y %I:%M %p")))

        duration = finishedDateTime - startDateTime
        print("Total execution time: {0} second(s)".format(duration.seconds))
        print("")

    except Exception: 
        print(Fore.RED + "Failed to run maintenance.")            
        traceback.print_exc()
        exit("" + Style.RESET_ALL)


computerMaintenance()
