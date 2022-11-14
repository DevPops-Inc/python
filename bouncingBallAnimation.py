#!/bin/python

# bouncing ball animation in Python

import colorama, os, sys, time, traceback
from colorama import Fore, Style
from datetime import datetime
from tkinter import * 
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

    print("Finisehd checking operating system at", datetime.now().strftime("%Y-%m-%d %H:%M %p"))

    print("")
    return operatingSystem


def bouncingBall():
    print("\nBouncing ball anmiation in Python.\n")
    checkOs()
    
    gui = Tk()
    gui.geometry("800x600")
    gui.title("Pi Animation")
    canvas = Canvas(gui,width=800,height=600,bg='white')
    canvas.pack()

    ball1 = canvas.create_oval(5,5,60,60, fill='red')

    xa = 5
    ya = 10

    try:
        startDateTime = datetime.now()

        print("Started bouncing ball animation at", startDateTime.strftime("%Y-%m-%d %H:%M %p"))

        while True: 
            canvas.move(ball1,xa,ya)
            pos=canvas.coords(ball1)
            if pos[3] >= 600 or pos[1] <= 0:
                ya = -ya
            if pos[2] >= 800 or pos[0] <= 0:
                xa = -xa
            gui.update()
            time.sleep(.025)
        
        print(Fore.GREEN + "Successfully ran bouncing ball animation." + Style.RESET_ALL)

        finishedDateTime = datetime.now()

        print("Finished bouncing ball animation at", finishedDateTime.strftime("%Y-%m-%d %H:%M %p"))

        duration = finishedDateTime - startDateTime
        print("Total execution time: {0} second(s)".format(duration.seconds))
        print("")
        
    except Exception as e:
        print(Fore.RED + "Failed to run bouncing ball animation.")
        print(e)
        print(traceback.print_stack)
        exit("" + Style.RESET_ALL)


bouncingBall()
