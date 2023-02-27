#!/bin/python

# falling ball in Python

# you can run this script with: python3 fallingBallInPython.py < background color > < fill color > 

import colorama, os, sys, time, traceback
from colorama import Fore, Style
from datetime import datetime
from tkinter import * 
colorama.init()


def checkOs(): 
    print("Started checking operating system at", datetime.now().strftime("%m-%d-%Y %I:%M %p"))

    if sys.platform == "win32": 
        print(Fore.GREEN + "Operating System:", end=""); sys.stdout.flush()
        os.system('ver')
        print(Style.RESET_ALL, end="")
        operatingSystem = "Windows"

    elif sys.platform == "darwin": 
        print(Fore.GREEN + "Operating System:")
        os.system('sw_vers')
        print(Style.RESET_ALL, end="")
        operatingSystem = "macOS"

    elif sys.platform == "linux": 
        print(Fore.GREEN + "Operating System:")
        os.system('uname -r')
        print(Style.RESET_ALL, end="")
        operatingSystem = "Linux"

    print("Finished checkig operating system at", datetime.now().strftime("%m-%d-%Y %I:%M %p"))
    print("")
    return operatingSystem


def getBackgroundColor(operatingSystem): 
    if operatingSystem == "Windows": 
        backgroundColor = str(input("Please type the background color and press the \"Enter\" key (Example: white): "))

    else: 
        backgroundColor = str(input("Please type the background color and press the \"return\" key (Example: white): "))

    print("")
    return backgroundColor


def getFillColor(operatingSystem): 
    if operatingSystem == "Windows": 
        fillColor = str(input("Please type the fill color and press the \"Enter\" key (Example: red): "))

    else: 
        fillColor = str(input("Please type the fill color and press the \"Enter\" key (Example: red): "))

    print("")
    return fillColor


def checkParameters(backgroundColor, fillColor): 
    print("Started checking parameter(s) at", datetime.now().strftime("%m-%d-%Y %I:%M %p"))
    valid = True

    print("Parameter(s):")
    print("--------------------------------------------")
    print("backgroundColor: {0}".format(backgroundColor))
    print("fillColor      : {0}".format(fillColor))
    print("--------------------------------------------")

    if backgroundColor == None: 
        print(Fore.RED + "backgroundColor is not set." + Style.RESET_ALL)
        valid = False

    if fillColor == None: 
        print(Fore.RED + "fillColor is not set." + Style.RESET_ALL)
        valid = False

    if valid == True: 
        print(Fore.GREEN + "All parameter check(s) passed." + Style.RESET_ALL)

        print("Finished checking parameter(s) at", datetime.now().strftime("%m-%d-%Y %I:%M %p"))
        print("")

    else: 
        print(Fore.RED + "One or more parameters are incorrect." + Style.RESET_ALL)

        print("Finished checking parameter(s) at", datetime.now().strftime("%m-%d-%Y %I:%M %p"))
        exit("")


def fallingBall(): 
    print("\nFalling ball in Python.\n")
    operatingSystem = checkOs()

    if len(sys.argv) >= 2: 
        backgroundColor = str(sys.argv[1])
        fillColor       = str(sys.argv[2])

    else: 
        backgroundColor = getBackgroundColor(operatingSystem)
        fillColor       = getFillColor(operatingSystem)

    checkParameters(backgroundColor, fillColor)

    try: 
        startDateTime = datetime.now()
        print("Started falling ball at", startDateTime.strftime("%m-%d-%Y %I:%M %p"))

        gui = Tk()
        gui.geometry("800x600")
        gui.title("Falling Ball in Python")
        canvas = Canvas(gui,width=800,height=600,bg=backgroundColor)
        canvas.pack()

        ball1 = canvas.create_oval(5,5,60,60, fill=fillColor)

        a = 5
        b = 5

        for x in range(0,100):
            canvas.move(ball1,a,b)
            gui.update()
            time.sleep(.01)

        gui.mainloop()
        print(Fore.GREEN + "Falling ball was successful." + Style.RESET_ALL)

        finishedDateTime = datetime.now()
        print("Finished falling ball at", finishedDateTime.strftime("%m-%d-%Y %I:%M %p"))

        duration = finishedDateTime - startDateTime
        print("Total execution time: {0} second(s)".format(duration.seconds))
        print("")

    except Exception: 
        print(Fore.RED + "Falling ball failed.")
        
        traceback.print_exc()
        exit("" + Style.RESET_ALL)


fallingBall()
