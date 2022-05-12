#!/bin/python

# check OS for Linux

import colorama, os, sys
from colorama import Fore, Style 
from datetime import datetime
colorama.init()

def checkOsForLinux(): 
    print("Started checking operating system at", datetime.now().strftime("%Y-%m-%d %H:%M %p"))

    if sys.platform == "linux":
        print(Fore.GREEN + "Operating System: ")
        print(os.system('uname -r'))
        print(Style.RESET_ALL)

        print("Finished checking operating system at", datetime.now().strftime("%Y-%m-%d %H:%M %p"))
        
        print("")
    else:
        print(Fore.RED + "Sorry this script only runs on Linux." + Style.RESET_ALL)
    
        print("Finished checking operating system at", datetime.now().strftime("%Y-%m-%d %H:%M %p"))
        
        exit("")

checkOsForLinux()
