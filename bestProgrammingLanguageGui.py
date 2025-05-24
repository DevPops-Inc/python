#!/bin/python

# best programming language GUI

import colorama, os, sys, traceback
from colorama import Fore, Style
from datetime import datetime
from tkinter import * 
colorama.init()


def checkOs():
    print("Started checking operating system at ", datetime.now().strftime("%m-%d-%Y %I:%M %p"))

    if sys.platform == "win32":
        print(Fore.GREEN + "Operating System:", end=""); sys.stdout.flush()
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
    
    print("Finished checking operating system at ", datetime.now().strftime("%m-%d-%Y %I:%M %p"))
    print("")
    return operatingSystem


def bestProgrammingLanguage():
    print("\nBest programming language GUI.\n")
    
    try:
        operatingSystem = checkOs()

        if operatingSystem == "Windows":
            input("Press any key to continue or press the \"Ctrl\" and \"C\" keys to quit: ")

        elif operatingSystem == "macOS" or operatingSystem == "Linux": 
            input("Press any key to continue or press the \"control\" and \"C\" keys to quit: ")

        print("")
        root = Tk()
        v = IntVar()
        
        startDateTime = datetime.now()
        
        print("Started best programming launch GUI at", startDateTime.strftime("%m-%d-%Y %I:%M %p"))

        Label(root, root.title("Options"), text="""What is the best programming language?""", justify = LEFT, padx = 20).pack()

        Radiobutton(root, text="Python", padx = 20, variable=v, value=1).pack(anchor=W)
        Radiobutton(root, text="C/C++", padx = 20, variable=v, value=2).pack(anchor=W)
        Radiobutton(root, text="JavaScript", padx = 20, variable=v, value=3).pack(anchor=W)
        Radiobutton(root, text="C#", padx = 20, variable=v, value=4).pack(anchor=W)
        Radiobutton(root, text="Java", padx = 20, variable=v, value=5).pack(anchor=W)
        Radiobutton(root, text="Go", padx = 20, variable=v, value=6).pack(anchor=W)
        Radiobutton(root, text="Rust", padx = 20, variable=v, value=7).pack(anchor=W)

        mainloop()

        print(Fore.GREEN + "Successfully ran best programming language GUI." + Style.RESET_ALL)

        finishedDatetime = datetime.now()

        print("Finished best programming language GUI at", finishedDatetime.strftime("%m-%d-%Y %I:%M %p"))

        duration = finishedDatetime - startDateTime
        print("Total execution time: {0} second(s)".format(duration.seconds))
        print("")
        
    except Exception as e:
        print(Fore.RED + "Failed to run best programming language GUI.")        
        traceback.print_exc()
        exit("" + Style.RESET_ALL)


bestProgrammingLanguage()
