#!/bin/python

import colorama, os, sys
from colorama import Fore, Style 
from datetime import datetime
colorama.init()

def checkOsForWindows(): 
    print("Checking operating system at", datetime.now().strftime("%Y-%m-%d %H:%M %p"))

    if sys.platform == "Windows":
        print(Fore.GREEN + "Operating System: Windows")
    else:
        sys.exit(Fore.RED + "Sorry this script only works on Windows")
    
    print(Style.RESET_ALL + "Finished checking operating system at", datetime.now().strftime("%Y-%m-%d %H:%M %p"))
    print("")

checkOsForWindows()
