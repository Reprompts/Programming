# Question 13: Write a Python program to calculate compound interest.
# Input:
# Principal = 2000
# Rate = 10
# Time = 2

# Output:
# Compound Interest = 420

# Explanation:
# Compound Interest is calculated using the formula:
# CI = P(1 + R/100)^T - P
# After calculation, the compound interest is 420.

# Asked In Companies:
# Practice Assignment

P = int(input("Enter the value of Principal: "))
R = int(input("Enter the value of Rate: "))
T = int(input("Enter the value of Time: "))

CI = P * ((1 + R/100)**T) - P

print("The Simple Interest is: ", CI)