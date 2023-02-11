#!/bin/python

# draw circle in Python

import colorama, os, sys, traceback, turtle
from colorama import Fore, Style
from datetime import datetime
colorama.init()


def checkOs(): 
    print("Started checking operating system at", datetime.now().strftime("%m-%d-%Y %I:%M %p"))

    if sys.platform == "win32": 
        print(Fore.GREEN + "Operating System:", end=""); sys.stdout.flush()
        os.system('ver')
        print(Style.RESET_ALL, end="")

    elif sys.platform == "darwin": 
        print(Fore.GREEN + "Operating System: ")
        os.system('sw_vers')
        print(Style.RESET_ALL, end="")

    elif sys.platform == "linux": 
        print(Fore.GREEN + "Operating System:")
        os.system('uname -r')
        print(Style.RESET_ALL, end="")

    print("Finished checking operating system at", datetime.now().strftime("%m-%d-%Y %I:%M %p"))
    print("")


def drawCircle(): 
    print("\nLet's draw a circle in Python!\n")
    checkOs()

    try: 
        startDateTime = datetime.now()
        print("Started drawing circle at", startDateTime.strftime("%m-%d-%Y %I:%M %p"))

        turtle.circle(50)
        turtle.getscreen()._root.mainloop()
        print(Fore.GREEN + "Successfully drew circle." + Style.RESET_ALL)

        finishedDateTime = datetime.now()
        print("Finished drawing circle at", finishedDateTime.strftime("%m-$d-%Y %I:%M %p"))

        duration = finishedDateTime - startDateTime
        print("Total execution time: {0} second(s)".format(duration.seconds))
        print("")

    except Exception: 
        print(Fore.RED + "Failed to draw circle.")
        
        traceback.print_exc()
        exit("" + Style.RESET_ALL)


drawCircle()
