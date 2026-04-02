# Question 6: Write a Python program to convert length from centimeter into meter and kilometer.'
# Input:
# Centimeter = 150
# Output:
# Meter = 1.5
# Kilometer = 0.0015
# Explanation:
# 1 meter = 100 centimeters
# 1 kilometer = 100000 centimeters
# The given value is converted using standard unit conversion formulas.

# Asked In Companies:
# Practice Assignment

Length = float(input("Enter the Length in Centimeter for the conversion: "))

Meter = Length * .01 
Kilometer = Length * .00001

print("The Length in Meters is: ", Meter)
print("The Lenght in Kilometers is: ", Kilometer)

