#!/bin/python

# defrag hard drive on Windows

# you can run this script with: python3 defragHardDriveOnWindows.py < answer > 

import colorama, os, sys, traceback
from colorama import Fore, Style
from datetime import datetime
colorama.init()


def checkOsForWindows():
    print("Start checking operating system at", datetime.now().strftime("%Y-%m-%d %H:%M %p"))

    if sys.platform == "win32": 
        print(Fore.GREEN + "Operating System: ")
        os.system('ver')

        print(Style.RESET_ALL + "Finished checking operating system at ", datetime.now().strftime("%Y-%m-%d %H:%M %p"))

        print("")
    else: 
        print(Fore.RED + "Sorry but this script only runs on Windows." + Style.RESET_ALL)

        print("Finished checking operating system at", datetime.now().strftime("%Y-%m-%d %H:%M %p"))

        exit("")


def getAnswer():
    os.system('PowerShell "Get-PhysicalDisk | Format-Table -AutoSize"')
    print("Do you want to defrag the HDD (not recommended for SSD drives)?")
    answer = str(input("Please press \"Y\" or \"N\" and press \"Enter\" key: "))
    
    print("")
    return answer


def checkParameters(answer):
    print("Started checking parameters at", datetime.now().strftime("%Y-%m-%d %H:%M %p"))
    valid = "true"

    print("Parameters:")
    print("--------------------------")
    print("answer: {0}".format(answer))
    print("--------------------------")

    if answer == None: 
        print(Fore.RED + "answer is not set." + Style.RESET_ALL)
        valid = "false"

    if valid == "true": 
        print(Fore.GREEN + "All parameter checks passed." + Style.RESET_ALL)

        print("Finished checking parameters at", datetime.now().strftime("%Y-%m-%d %H:%M %p"))
        print("")
    else: 
        print(Fore.RED + "One or more parameters are incorrect." + Style.RESET_ALL)

        print("Finished checking parameters at", datetime.now().strftime("%Y-%m-%d %H:%M %p"))
        print("")


def defragHardDrive():
    print("\nDefrag Hard Drive on Windows.\n")
    checkOsForWindows()

    if len(sys.argv) >= 2: 
        answer  = str(sys.argv[1]) 
    else: 
        answer = getAnswer()

    checkParameters(answer)

    try: 
        startDateTime = datetime.now()
        print("Started getting hard drive info at ", startDateTime.strftime("%Y-%m-%d %H:%M %p"))

        if answer == "Y" or answer == "y":
            os.system('defrag c: /u')

        print(Fore.GREEN + "Successfully got hard drive info." + Style.RESET_ALL)
        
        finishedDateTime = datetime.now()
        
        print("Finished getting hard drive info at ", finishedDateTime.strftime("%Y-%m-%d %H:%M %p"))

        duration = finishedDateTime - startDateTime
        print("Total execution time: {0} second(s)".format(duration.seconds))
        print("")
    except Exception as e: 
        print(Fore.RED + "Failed to get hard drive info.")
        print(e)
        print(traceback.print_stack)
        exit("" + Style.RESET_ALL)


defragHardDrive()
