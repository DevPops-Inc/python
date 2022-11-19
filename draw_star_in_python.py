#!/bin/python

# draw a star with turtle

import colorama, os, sys, traceback
from colorama import Fore, Style
from datetime import datetime
from turtle import *
colorama.init()


def checkOs(): 
    print("Started checking operating system at", datetime.now().strftime("%Y-%m-%d %H:%M %p"))
    
    if sys.platform == "win32":
        print(Fore.GREEN + "Operating System: ", end="")
        os.system('ver')
        print(Style.RESET_ALL, end="")
        operatingSystem = "Windows"

    elif sys.platform == "darwin": 
        print(Fore.GREEN + "Operating System: ")
        os.system('sw_vers')
        print(Style.RESET_ALL, end="")
        operatingSystem = "macOS"

    elif sys.platform == "linux": 
        print(Fore.GREEN + "Operating System: ")
        os.system('uname -r')
        print(Style.RESET_ALL, end="")
        operatingSystem = "Linux"

    print("Finished checking operating system at", datetime.now().strftime("%Y-%m-%d %H:%M %p"))
    print("")
    return operatingSystem


def drawStar(): 
    print("\nLet's draw a star in Python!\n")
    checkOs()

    try: 
        startDateTime = datetime.now()
        print("Started drawing star at", startDateTime.strftime("%Y-%m-%d %H:%M %p"))

        color('orange', 'yellow')

        begin_fill()
        while True:
            forward(200)
            left(170)
            if abs(pos()) < 1:
                break
        end_fill()
        done()

        print(Fore.GREEN + "Successfully drew star in Python.")

        finishedDateTime = datetime.now()
        print("Finished drawing star at", finishedDateTime.strftime("%Y-%m-%d %H:%M %p"))

        duration = finishedDateTime - startDateTime
        print("Total execution time: {0} second(s)".format(duration.seconds))
        print("")

    except Exception as e: 
        print(Fore.RED + "Failed to draw star.")
        print(e)
        print(traceback.print_stack)
        exit("" + Style.RESET_ALL)


drawStar()
