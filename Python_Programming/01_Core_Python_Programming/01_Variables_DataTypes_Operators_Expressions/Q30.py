# Question 30: Write a Python program to check whether a number is a multiple of both 3 and 5.
# Input:
# 15

# Output:
# Multiple of both 3 and 5

# Explanation:
# A number divisible by both 3 and 5 must give remainder 0 when divided by 3 and by 5.
# The logical AND operator is used to check both conditions.

# Asked In Companies:
# Practice Assignment

Num = int(input("Enter a number to check if it's divisible by 3 and 5: "))

if Num % 3 == 0 and Num % 5 == 0:
    print("The number is divisible by 3 and 5!")
else:
    print("The number is not divisible by 3 and 5!")