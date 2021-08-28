#!/bin/python

import colorama, os, sys
from colorama import Fore, Style 
from datetime import datetime
colorama.init()

def checkOsForLinux(): 
    print("Checking operating system at", datetime.now().strftime("%Y-%m-%d %H:%M %p"))

    if sys.platform == "Linux":
        print(Fore.GREEN + "Operating System: Linux")
    else:
        sys.exit(Fore.RED + "Sorry this script only works on Linux")
    
    print(Style.RESET_ALL + "Finished checking operating system at", datetime.now().strftime("%Y-%m-%d %H:%M %p"))
    print("")

checkOsForLinux()
