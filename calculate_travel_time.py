#!/bin/python

# calculate travel time

# prompt user input
str(input("Calculate travel time.\nPress any key to continue.\n"))

print("Input a rate and a distance\n")
rate = float(input("Rate (Miles per Hour): \n"))
distance = float(input("Distance (Miles): \n"))

print("Time (Hours):", (distance / rate))
