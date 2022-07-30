#!/bin/python

# Windows maintenance

# run this script as admin

import colorama, os, sys, traceback
from colorama import Fore, Style 
from datetime import datetime
colorama.init()

def checkOsForWindows():
    print("Started checking operating system at ", datetime.now().strftime("%Y-%m-%d %H:%M %p"))

    if sys.platform == "win32": 
        print(Fore.GREEN + "Operating System: ")
        print(os.system('ver'))
        
        print(Style.RESET_ALL + "Finished checking operating system at ", datetime.now().strftime("%Y-%m-%d %H:%M %p"))

        print("")

    else: 
        print(Fore.RED + "Sorry but this script only runs on Windows." + Style.RESET_ALL)

        print("Finished checking operating system at ", datetime.now().strftime("%Y-%m-%d %H:%M %p"))

        exit("")
    

def runWindowsMaintenance():
    print("\nRun Windows maintenance.\n")
    checkOsForWindows()

    try: 
        startDateTime = datetime.now()
        
        print("Started running Windows maintenance at ", startDateTime.strftime("%Y-%m-%d %H:%M %p"))

        maintenance = ['echo y | chkdsk /f/r c:', 'SFC /scannow', 'Dism /Online /Cleanup-Image /ScanHealth']

        for job in maintenance: 
            os.system(job)

        os.system('PowerShell "Get-PhysicalDisk | Format-Table -AutoSize"')
        print("Do you want to defrag the HDD (not recommended for SSD drives)?")
        answer = str(input("Please press \"Y\" or \"N\" and press \"Enter\" key: "))
        if answer == "Y" or answer == "y":
            os.system('defrag c: /u')
            
        print(Fore.GREEN + "Successfully ran maintenance on Windows." + Style.RESET_ALL)

        finishedDateTime = datetime.now()

        print("Finished running Windows maintenance at ", finishedDateTime.strftime("%Y-%m-%d %H:%M %p"))

        duration = finishedDateTime - startDateTime 
        print("Total execution time: {0} second(s)".format(duration.seconds))
        print("")

        print("Please save your work and close applications.")
        str(input("Press any key to continue."))
        os.system('shutdown /r /t 0')
        
    except Exception as e: 
        print(Fore.RED + "Failed to run maintenance on Windows.")
        print(e)
        print(traceback.print_stack)
        exit("" + Style.RESET_ALL)

runWindowsMaintenance()
