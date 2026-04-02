# Question 24: Write a Python program to check whether a number is a Neon number or not.
# Input:
# 9

# Output:
# Neon Number

# Explanation:
# A Neon number is a number where the sum of digits of its square is equal to the number itself.
# 9² = 81 ? 8 + 1 = 9.

# Asked In Companies:
# Practice Assignment

Num = int(input("Enter a number from 0 to 9: "))

Square = Num ** 2

Sum_digits = (Square % 10) + (Square // 10)

if Num == Sum_digits:
    print("The given number is Neon Number!")
else:
    print("The given number is not a Neon Number!")