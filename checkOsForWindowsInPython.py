#!/bin/python

# check OS for Windows

import colorama, os, sys
from colorama import Fore, Style 
from datetime import datetime
colorama.init()


def checkOsForWindows(): 
    print("Started checking operating system at", datetime.now().strftime("%m-%d-%Y %I:%M %p"))

    if sys.platform == "Windows":
        print(Fore.GREEN + "Operating System:", end=""); sys.stdout.flush()
        os.system('ver')
        print(Style.RESET_ALL, end="")

        print("Finished checking operating system at", datetime.now().strftime("%m-%d-%Y %I:%M %p"))
        
        print("")
        
    else:
        print(Fore.RED + "Sorry this script only runs on Windows." + Style.RESET_ALL)
    
        print("Finished checking operating system at", datetime.now().strftime("%m-%d-%Y %I:%M %p"))
        
        exit("")


checkOsForWindows()
