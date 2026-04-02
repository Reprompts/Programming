# Question 5: Write a Python program to enter the radius of a circle and calculate its diameter, area, and circumference.
# Input:
# Radius = 7

# Output:
# Diameter = 14
# Area = 153.86
# Circumference = 43.96

# Explanation:
# Diameter = 2 × radius
# Area = ? × r²
# Circumference = 2 × ? × r
# The formulas are applied using the given radius.

# Asked In Companies:
# Practice Assignment

from math import pi

Radius = int(input("Enter the radius of the circle: "))

Diameter = 2 * Radius
Area = pi * Radius**2
Circum = 2 * pi * Radius 

print("The Diameter of the circle is: ", Diameter)
print("The Area of the circle is: ", Area)
print("The Circumeference of the circle is: ", Circum)
