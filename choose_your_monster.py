#!/bin/python

# choose your monster

# import Tkinter module 
from tkinter import *
root = Tk()

# define function 
def chooseMonster():
    print("Vampire: %d, \nWerewolf: %d" % (var1.get(), var2.get()))
Label(root, root.title("Vampire vs. Werewolf"), text="Choose your monster!").grid(row=0, 
stick=N)

# declare variables
var1 = IntVar()
Checkbutton(root, text="Vampire", variable=var1).grid(row=1, sticky=W)
var2 = IntVar()
Checkbutton(root, text="Werewolf", variable=var2).grid(row=2, sticky=W)
Button(root, text='Quit', command=root.destroy).grid(row=3, sticky=W, pady=4)
Button(root, text='Show', command=chooseMonster).grid(row=3, sticky=E, pady=4)

mainloop()
