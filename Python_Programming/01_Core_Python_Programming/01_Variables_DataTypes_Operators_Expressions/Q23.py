# Question 23: Write a Python program to calculate the sum of the first and last digit without using a loop.
# Input:
# 123

# Output:
# 4

# Explanation:
# First digit = 1
# Last digit = 3
# Sum = 1 + 3 = 4.

# Asked In Companies:
# Practice Assignment

Num = 123

First = Num // 100
Last = Num % 10

print("The first digit is: ", First)
print("The last digit is: ", Last)

print("The sum of first and last digit is: ", First + Last)
