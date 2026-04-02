# Question 22: Write a Python program to find the first and last digit of a three-digit number without using a loop.
# Input:
# 456

# Output:
# First = 4
# Last = 6

# Explanation:
# The first digit is obtained by dividing the number by 100.
# The last digit is obtained using the modulus operator (% 10).

# Asked In Companies:
# Practice Assignment


# Later I want to design a program in which I can dynamically increase the value in the steps of 10 for Base division of Num so that I can find the value of the num in the future with any number of digits 

Num = 456

First = Num // 100
Last = Num % 10

print("The first digit is: ", First)
print("The last digit is: ", Last)
