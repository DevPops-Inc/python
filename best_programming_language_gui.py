#!/bin/python

# best programming language GUI

# import tkinter module 
from tkinter import * 

# prompt user input
str(input("Best programming language GUI.\nPress any key to continue or press Ctrl and C keys to quit.\n"))

# declare variables
root = Tk()
v = IntVar()

# create GUI label 
Label(root, root.title("Options"), text="""What is the best programming language?""", justify = LEFT, padx = 20).pack()

# crreate radio buttons
Radiobutton(root, text="Python", padx = 20, variable=v, value=1).pack(anchor=W)
Radiobutton(root, text="C/C++", padx = 20, variable=v, value=2).pack(anchor=W)
Radiobutton(root, text="JavaScript", padx = 20, variable=v, value=3).pack(anchor=W)
Radiobutton(root, text="C#", padx = 20, variable=v, value=4).pack(anchor=W)
Radiobutton(root, text="Java", padx = 20, variable=v, value=5).pack(anchor=W)
Radiobutton(root, text="Go", padx = 20, variable=v, value=6).pack(anchor=W)
Radiobutton(root, text="Rust", padx = 20, variable=v, value=7).pack(anchor=W)

# call main loop
mainloop()
