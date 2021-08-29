#!/bin/python 

# allow apps downloaded from anywhere on Mac

import colorama, os, sys, time, traceback
from colorama import Fore, Style 
from datetime import datetime
colorama.init()

def checkOsForMac(): 
    print("Checking operating system at", datetime.now().strftime("%Y-%m-%d %H:%M %p"))

    if sys.platform == "darwin":
        print(Fore.GREEN + "Operating System: macOS")
        print(os.system('sw_vers'))
    else:
        sys.exit(Fore.RED + "Sorry this script only works on macOS")
    
    print(Style.RESET_ALL + "Finished checking operating system at", datetime.now().strftime("%Y-%m-%d %H:%M %p"))
    print("")

def allowAppsDownloadedFromAnywhere():
    print("\nAllow apps downloaded from anywhere on Mac.\n")
    checkOsForMac()

    print("Started allowing apps downloaded from anywhere at", datetime.now().strftime("%Y-%m-%d %H:%M %p"))
    start=time.process_time()

    try: 
        os.system('sudo spctl --master-disable')

        print("\nExpand Apple menu and select \"System Preferences...\"\nSelect \"Security & Privacy.\"\nSelect \"General\" tab and you will see \"Anywhere\" option under \"Allow apps downloaded from:\" list now.\nSelect the lock icon and log in with your credentials.\nSelect \"Anywhere\" to allow apps to be downloaded from anywhere on your Mac.\n")

        print(Fore.GREEN + "Successfully allowed apps downloaded from anywhere" + Style.RESET_ALL)

        print("Finished allowing apps downloaded from anywhere at", datetime.now().strftime("%Y-%m-%d %H:%M %p"))

        print("Total execution time: {0} second(s)".format(time.process_time() - start))

    except Exception as e: 
        print(Fore.RED + "Failed to allow apps downloaded from anywhere.")
        print(e)
        print(traceback.print_stack())
        print(Style.RESET_ALL)

allowAppsDownloadedFromAnywhere()
