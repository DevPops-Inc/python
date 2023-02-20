#!/bin/python

# stop and relaunch Outlook on Windows 

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


def stopAndRelaunchOutlook(): 
    print("\nStop and relaunch Outlook on Windows.\n")
    checkOsForWindows()

    outlookApp = 'outlook.exe'
    stopOutlook = 'taskkill /F /IM {0}'.format(outlookApp)
    outlookPath = r"C:\\Program Files\\Microsoft Office\\root\\Office16\\OUTLOOK.EXE"
    relaunchOutlook = 'explorer {0}'.format(outlookPath)

    try: 
        startDateTime = datetime.now()
        
        print("Started stopping and relauching Outlook at", startDateTime.strftime("%m-%d-%Y %I:%M %p"))

        outlookTasks = [ stopOutlook, relaunchOutlook]

        for task in outlookTasks: 
            if os.system(task) != 0: 
                raise Exception("Attempt threw an error!")
            
        print(Fore.GREEN + "Successfully stopped and relaunched Outlook." + Style.RESET_ALL)

        finishedDateTime = datetime.now()

        print("Finished stopping and relaunching Outlook at", finishedDateTime.strftime("%m-%d-%Y %I:%M %p"))

        duration = finishedDateTime - startDateTime
        print("Total execution time: {0} second(s)".format(duration.seconds))
        print("")

    except Exception: 
        print(Fore.RED + "Failed to stop and relaunch Outlook.")
        traceback.print_exc()
        exit("" + Style.RESET_ALL)


stopAndRelaunchOutlook()
