#!/bin/python 

# macOS maintenance 

# you can run this script with: python3 macOsMaintenance.py < 1 for "Macintosh HD" or 2 for "MacOS" > 

import colorama, os, sys, traceback
from colorama import Fore, Style
from datetime import datetime
colorama.init()


def checkOsForMac():
    print("Started checking operating system at ", datetime.now().strftime("%Y-%m-%d %H:%M %p"))

    if sys.platform == "darwin":
        print(Fore.GREEN + "Operating System:")
        os.system('sw_vers')
        
        print(Style.RESET_ALL + "Finished checking operating system at ", datetime.now().strftime("%Y-%m-%d %H:%M %p"))

        print("")

    else: 
        print(Fore.RED + "Sorry but this script only works on Mac" + Style.RESET_ALL)

        print("Finished checking operating system at ", datetime.now().strftime("%Y-%m-%d %H:%M %p"))

        exit("")


def getHardDrive():
    os.system('diskutil list')

    answer = str(input("Please type 1 if your hard drive is \"Macintosh HD\" or 2 if it's \"MacOS\" and press \"return\" key: "))
    
    if answer == "1": 
        hdd = "Macintosh HD"
    elif answer == "2": 
        hdd = "MacOS"

    print("")
    return hdd


def checkParameters(hdd):
    print("Started checking parameters at ", datetime.now().strftime("%Y-%m-%d %H:%M %p"))
    valid = "true"

    print("Parameters:")
    print("--------------------")
    print("hdd: {0}".format(hdd))
    print("--------------------")

    if hdd == None: 
        print(Fore.RED + "hdd is not set." + Style.RESET_ALL)
        valid = "false"

    if valid == "true":
        print(Fore.GREEN + "All parameter checks passed." + Style.RESET_ALL)

        print("Finished checking parameters at ", datetime.now().strftime("%Y-%m-%d %H:%M %p"))

        print("")

    else: 
        print(Fore.RED + "One or more parameters are incorrect." + Style.RESET_ALL)

        print("Finished checking parameters at ", datetime.now().strftime("%Y-%m-%d %H:%M %p"))

        exit("")

    
def runMacMaintenance():
    print("\nRun Mac maintenance.\n")
    checkOsForMac()

    if len(sys.argv) > 2: 
        hdd = str(sys.argv[1])

    else: 
        hdd = getHardDrive()

    checkParameters(hdd)

    try: 
        startDateTime = datetime.now()
        
        print("Started running Mac maintenance at ", startDateTime.strftime("%Y-%m-%d %H:%M %p"))

        maintenance = ['sudo mdutil -i on /', 'softwareupdate --install --all']

        for jobs in maintenance: 
            os.system(jobs)

        if hdd == "Macintosh HD": 
            os.system('diskutil verifyVolume "Macintosh HD"')
            os.system('diskutil repairVolume "Macintosh HD"')

        elif hdd == "MacOS": 
            os.system('diskutil verifyVolume MacOS')
            os.system('diskutil repairVolume MacOS')

        print(Fore.GREEN + "Successfully ran Mac maintenance." + Style.RESET_ALL)

        finishedDateTime = datetime.now()

        print("Finished running Mac maintenance at ", finishedDateTime.strftime("%Y-%m-%d %H:%M %p"))

        duration = finishedDateTime - startDateTime
        print("Total execution time: {0} second(s)".format(duration.seconds))
        print("")

        print("Please save your documents and close applications.")
        str(input("Press any key to restart Mac."))
        os.system('reboot')
        
    except Exception as e: 
        print(Fore.RED + "Failed to run Mac maintenance.")
        print(e)
        print(traceback.print_stack)
        exit("" + Style.RESET_ALL)
        

runMacMaintenance()
