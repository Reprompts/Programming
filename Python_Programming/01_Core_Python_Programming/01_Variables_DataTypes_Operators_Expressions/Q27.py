# Question 27: Write a Python program to toggle the case of an alphabet using ASCII values.
# Input:
# a

# Output:
# A

# Explanation:
# Lowercase and uppercase letters differ by 32 in ASCII values.
# By adding or subtracting 32, the case of the alphabet can be changed.

# Asked In Companies:
# Practice Assignment

Character = input("Enter the character you want to change case of: ")

print(chr(ord(Character) - 32))

