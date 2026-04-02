# Question 12: Write a Python program to calculate simple interest.
# Input:
# Principal = 1000
# Rate = 5
# Time = 2

# Output:
# Simple Interest = 100

# Explanation:
# Simple Interest formula:
# SI = (Principal × Rate × Time) / 100
# Applying the formula gives 100.

# Asked In Companies:
# Practice Assignment

P = int(input("Enter the value of Principal: "))
R = int(input("Enter the value of Rate: "))
T = int(input("Enter the value of Time: "))

SI = (P * R * T) / 100 

print("The Simple Interest is: ", SI)