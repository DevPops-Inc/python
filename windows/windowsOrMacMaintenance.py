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

    maintenance = ['sudo mdutil -i on /', 'softwareupdate --install --all']

    for jobs in maintenance: 
        os.system(jobs)

    os.system('diskutil list')

    answer = str(input("Please type 1 if your hard drive is \"Macintosh HD\" or 2 if it's \"MacOS\" and press \"return\" key: ")) # TODO: iterate to get disk name
    
    if answer == "1": 
        os.system('diskutil verifyVolume "Macintosh HD"')
        os.system('diskutil repairVolume "Macintosh HD"')

    elif answer == "2": 
        os.system('diskutil verifyVolume MacOS')
        os.system('diskutil repairVolume MacOS')

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
        except Exception as e: 
            print(Fore.RED + "Failed to run Windows maintenance.")
            print(e)
            print(traceback.print_stack)
            exit("" + Style.RESET_ALL)
            
    elif operatingSystem == "macOS":
        try: 
            runMacMaintenance()
        except Exception as e: 
            print(Fore.RED + "Failed to run Mac maintenance.")
            print(e)
            print(traceback.print_stack)
            exit("" + Style.RESET_ALL)


computerMaintenance()
