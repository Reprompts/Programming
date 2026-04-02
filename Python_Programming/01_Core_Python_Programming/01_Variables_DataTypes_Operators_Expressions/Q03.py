# Question 3: Write a Python program to enter two numbers and perform addition, subtraction, multiplication, division, and modulus.
# Input:
# Number1 = 20
# Number2 = 5

# Output:
# Addition = 25
# Subtraction = 15
# Multiplication = 100
# Division = 4
# Modulus = 0

# Explanation:
# The program performs all basic arithmetic operations using the two given numbers and displays the results.

# Asked In Companies:
# Practice Assignment

Num1 = float(input("Enter the first number: "))
Num2 = float(input("Enter the second number: "))

sum = Num1 + Num2 
sub = Num1 - Num2
mul = Num1 * Num2 
div = Num1 / Num2 
mod = Num1 % Num2 

print("The result of sum is: ", sum)
print("The result of sub is: ", sub)
print("The result of mul is: ", mul)
print("The result of div is: ", div)
print("The result of mod is: ", mod)