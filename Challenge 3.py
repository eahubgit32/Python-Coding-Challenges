# Challenge 3: Volume of a Cylinder
# Write a Python program that calculates the volume of a
# cylinder given its radius and height.


import math

def VolumeOfCylinder(radius, height):
    volume = math.pi * (radius ** 2) * height
    print(f"Volume of the cylinder: {volume:.2f}")

radius = float(input("Enter the Radius of the cylinder: "))
height = float(input("Enter the height of the cylinder: "))

VolumeOfCylinder(radius, height)





