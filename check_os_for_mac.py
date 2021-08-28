#!/bin/python

import colorama, os, sys
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

checkOsForMac()
