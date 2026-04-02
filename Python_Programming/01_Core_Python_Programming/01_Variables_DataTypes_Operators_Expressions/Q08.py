# Question 8: Write a Python program to convert temperature from Celsius to Fahrenheit.
# Input:
# Celsius = 37

# Output:
# Fahrenheit = 98.6

# Explanation:
# The formula used is:
# F = (C × 9 / 5) + 32
# The Celsius value is converted into Fahrenheit using this formula.

# Asked In Companies:
# Practice Assignment

C = float(input("Enter the temperature in Celcius: "))

F = (C * 9/5) + 32 

print("The temeprature in Fahrenheit is: ", F)