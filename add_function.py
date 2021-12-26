#!/bin/python

# add function

import colorama, os, sys, time, traceback
from colorama import Fore, Style 
from datetime import datetime
colorama.init()

def addFuction():
    print("\nLet's add in Python!\n")

    if sys.platform == "Windows":
        print(Fore.GREEN + "Operating System: Windows" + Style.RESET_ALL)
        a = int(input("Type first number and press \"Enter\" key (Example: 2): "))
        b = int(input("Type second number and press \"Enter\" key (Example: 2): "))
    elif sys.platform == "darwin":
        print(Fore.GREEN + "Operating System: macOS" + Style.RESET_ALL)
        a = int(input("Type first number and press \"return\" key (Example: 2): "))
        b = int(input("Type second number and press \"return\" key (Example: 2): "))
    elif sys.platform == "Linux":
        print(Fore.GREEN + "Operating System: Linux" + Style.RESET_ALL)
        a = int(input("Type first number and press \"return\" key (Example: 2): "))
        b = int(input("Type second number and press \"return\" key (Example: 2): "))
    
    try: 
        print("\nStarted adding at", datetime.now().strftime("%Y-%m-%d %H:%M %p"))
        start=time.process_time()

        result = a + b 
        print(Fore.YELLOW + "The result is:", result)
        
        print(Fore.GREEN + "Successfully added in Python" + Style.RESET_ALL)
        print("Finished adding at", datetime.now().strftime("%Y-%m-%d %H:%M %p"))
        
        print("Total execution time: {0} second(s)".format(round(time.process_time() - start)))

        print("")

    except Exception as e: 
        print(Fore.RED + "Failed to add in Python.")
        print(e)
        print(traceback.print_stack)
        print(Style.RESET_ALL)
        
addFuction()
