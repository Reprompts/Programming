# Question 20: Write a Python program to compute the sum of digits of an integer.
# Input:
# 123

# Output:
# 6

# Explanation:
# Each digit is separated using modulus and division operations.
# 1 + 2 + 3 = 6.

# Asked In Companies:
# Practice Assignment

Num = int(input("Enter the number to find sum of its digits: "))
Sum = 0

while Num:
    Sum += Num % 10
    Num = Num // 10

print("The sum of the all the digits of the number is: ", Sum)