# Question 21: Write a Python program to reverse a number without using a loop.
# Input:
# 123

# Output:
# 321

# Explanation:
# Digits are separated using arithmetic operations and rearranged in reverse order without using loops.

# Asked In Companies:
# Practice Assignment

Value = 123

a = Value % 10
b = (Value // 10) % 10
c = (Value // 100)

reverse = (a * 100) + (b * 10) + c

print("The reverse of the Number is: ", reverse)