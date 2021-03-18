#!/bin/python

# calculate travel time

print("Input a rate and a distance")
rate = float(input("Rate (Miles per Hour): "))
distance = float(input("Distance (Miles): "))

print("Time (Hours):", (distance / rate))
