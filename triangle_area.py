# This line imports the sys library, which allows us to use command line arguments.
import sys

# This line imports the math library, which allows us to use the square root function.
import math

# This line prints a welcome message to the user.
print("Welcome to the Triangle Area Calculator!")

# This line asks the user to input the first side of the triangle and stores it as a float (a decimal number).
side_a = float(input("Please enter the first side of the triangle: "))

# This line asks the user to input the second side of the triangle and stores it as a float.
side_b = float(input("Please enter the second side of the triangle: "))

# This line asks the user to input the third side of the triangle and stores it as a float.
side_c = float(input("Please enter the third side of the triangle: "))

# This line calculates the semi-perimeter (s) of the triangle by adding the three sides and dividing by 2.
semi_perimeter = (side_a + side_b + side_c) / 2

# This line uses Heron's formula to calculate the area of the triangle.
area = math.sqrt(semi_perimeter * (semi_perimeter - side_a) * (semi_perimeter - side_b) * (semi_perimeter - side_c))

# This line prints the calculated area, formatted as a string with two decimal places.
print("The area of the triangle is: {:.2f}".format(area))

# This line pauses the script and waits for the user to press the Enter key before exiting.
input("Press Enter to exit.")
