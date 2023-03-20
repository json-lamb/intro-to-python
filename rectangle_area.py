# This line imports the sys library, which allows us to use command line arguments.
import sys

# This line prints a welcome message to the user.
print("Welcome to the Rectangle Area Calculator!")

# This line asks the user to input the length of the rectangle and stores it as a float (a decimal number).
length = float(input("Please enter the length of the rectangle: "))

# This line asks the user to input the width of the rectangle and stores it as a float.
width = float(input("Please enter the width of the rectangle: "))

# This line calculates the area of the rectangle by multiplying the length and width.
area = length * width

# This line prints the calculated area, formatted as a string with two decimal places.
print("The area of the rectangle is: {:.2f}".format(area))

# This line pauses the script and waits for the user to press the Enter key before exiting.
input("Press Enter to exit.")
