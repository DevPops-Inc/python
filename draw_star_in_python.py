#!/bin/python

# draw a star with turtle

# import from turtle module 
from turtle import *

# prompt user input
str(input("\nDraw a star with turtle module.\nPress any key to continue or press Ctrl and C keys to quit.\n"))

# color star red with yellow border
color('orange', 'yellow')

# while loop to draw star
begin_fill()
while True:
    forward(200)
    left(170)
    if abs(pos()) < 1:
        break
end_fill()
done()
