# Challenge 2: Area of a Rectangle
# Write a Python program that calculates the area of a
# rectangle given its length and width.

def AreaOfRectangle(length, width):
    Area = round(length * width, 2)
    print("Are of a rectangle: ", Area)


length = float(input("Enter the length of the triangle: "))
width = float(input("Enter the width of the triangle: "))

AreaOfRectangle(length, width)