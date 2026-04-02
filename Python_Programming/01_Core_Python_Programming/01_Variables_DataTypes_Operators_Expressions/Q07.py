# Question 7: Write a Python program to convert temperature from Fahrenheit to Celsius.
# Input:
# Fahrenheit = 98

# Output:
# Celsius = 36.67

# Explanation:
# The formula used is:
# C = (F ? 32) × 5 / 9
# Applying the formula gives the Celsius temperature.

# Asked In Companies:
# Practice Assignment

F = float(input("Enter the temprature in Fahrenheit: "))

C = (F - 32) * 5 / 9

print("The temperature in celcius is: ", C)

