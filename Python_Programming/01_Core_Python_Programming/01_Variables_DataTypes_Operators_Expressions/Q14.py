# Question 14: Write a Python program to swap two numbers using a third variable.
# Input:
# A = 5
# B = 10

# Output:
# A = 10
# B = 5

# Explanation:
# A temporary variable is used to store one value while swapping the numbers.

# Asked In Companies:
# Practice Assignment

A = 5 
B = 10

print("Before swapping A: ", A)
print("Before swapping B: ", B)

C = A 
A = B 
B = C

print("The Swapped number A: ", A)
print("The Swaped number B: ", B)