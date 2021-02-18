#!/bin/python

# draw a star with turtle

# import from turtle module 
from turtle import *

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
