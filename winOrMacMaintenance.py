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
        print(Fore.RED + "Sorry but this script only runs on Windows or macOS." + Style.RESET_ALL)

        print("Finished checking operating system at ", datetime.now().strftime("%m-%d-%Y %I:%M %p"))
        exit("")

    print("Finished checking operating system at ", datetime.now().strftime("%m-%d-%Y %I:%M %p"))
    print("")
    return operatingSystem
    

def runWindowsMaintenance():
    startDateTime = datetime.now()
    
    print("Started running Windows maintenance at ", startDateTime.strftime("%m-%d-%Y %I:%M %p"))

    maintenance = ['echo y | chkdsk /f/r c:', 'SFC /scannow', 'Dism /Online /Cleanup-Image /ScanHealth']

    for job in maintenance: 
        os.system(job)

    os.system('PowerShell "Get-PhysicalDisk | Format-Table -AutoSize"') # TODO: iterate to get HDD vs SDD
    print("Do you want to defrag the HDD (not recommended for SSD drives)?")
    
    answer = str(input("Please press \"Y\" or \"N\" and press \"Enter\" key: "))

    if answer == "Y" or answer == "y":
        os.system('defrag c: /u')

    print(Fore.GREEN + "Successfully ran maintenance on Windows." + Style.RESET_ALL)

    finishedDateTime = datetime.now()

    print("Finished running Windows maintenance at ", finishedDateTime.strftime("%m-%d-%Y %I:%M %p"))

    duration = finishedDateTime - startDateTime 
    print("Total execution time: {0} second(s)".format(duration.seconds))
    print("")
    
    print("Please save your work and close applications.")
    str(input("Press any key to continue."))
    os.system('shutdown /r /t 0')


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
    
    verifyVolume = 'distutil verifyVolume "{0}"'.format(hdd)
    
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
    os.system('reboot')


def computerMaintenance():
    print("\nRun computer maintenance.\n")
    operatingSystem = checkOs()

    if operatingSystem == "Windows": 
        try: 
            runWindowsMaintenance()
        except Exception: 
            print(Fore.RED + "Failed to run Windows maintenance.")
            
            traceback.print_exc()
            exit("" + Style.RESET_ALL)
            
    elif operatingSystem == "macOS":
        try: 
            runMacMaintenance()
        except Exception: 
            print(Fore.RED + "Failed to run Mac maintenance.")
            
            traceback.print_exc()
            exit("" + Style.RESET_ALL)


computerMaintenance()
