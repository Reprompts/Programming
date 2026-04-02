# Question 26: Write a Python program to check whether a number is a Spy number.
# Input:
# 1412

# Output:
# Spy Number

# Explanation:
# A Spy number is a number where the sum of digits equals the product of digits.
# Sum = 1 + 4 + 1 + 2 = 8
# Product = 1 × 4 × 1 × 2 = 8.

# Asked In Companies:
# # Practice Assignment

Num = int(input("Enter the number to check if it's a spy: "))
Sum = 0
Product = 1

while Num:
    digit = Num % 10
    Num = Num // 10
    Sum += digit
    Product *= digit 

if Sum == Product:
    print("This number is a spy number!")
else:
    print("The number is not a spy number!")