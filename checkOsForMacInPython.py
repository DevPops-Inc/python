#!/bin/python

# check OS for Mac

import colorama, os, sys
from colorama import Fore, Style 
from datetime import datetime
colorama.init()

def checkOsForMac(): 
    print("Start checking operating system at", datetime.now().strftime("%Y-%m-%d %H:%M %p"))

    if sys.platform == "darwin":
        print(Fore.GREEN + "Operating System: ")
        print(os.system('sw_vers'))
        print(Style.RESET_ALL)
        
        print("Finished checking operating system at", datetime.now().strftime("%Y-%m-%d %H:%M %p"))

        print("")
    else:
        print(Fore.RED + "Sorry this script only works on macOS." + Style.RESET_ALL )
    
        print("Finished checking operating system at", datetime.now().strftime("%Y-%m-%d %H:%M %p"))

        exit("")

checkOsForMac()
