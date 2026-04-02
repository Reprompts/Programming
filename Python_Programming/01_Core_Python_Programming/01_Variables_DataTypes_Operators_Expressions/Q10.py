# Question 10: Write a Python program to calculate the area of an equilateral triangle.
# Input : Side = 6
# Output : Area = 15.59
# Explanation : Area is calculated using the formula for equilateral triangles.

# Asked In Companies:
# Practice Assignment


# Area = 1/2 * side * Base 

from math import sqrt

Side = float(input("Enter the value of the side: "))

Area = (sqrt(3)/4) * Side**2

print("Area of the equilateral triangle with the given side is: ", Area)