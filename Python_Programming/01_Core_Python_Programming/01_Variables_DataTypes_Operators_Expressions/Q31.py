# Question 31: Write a Python program to check whether a given number is even or odd.
# Input:
# Number = 12

# Output:
# Even

# Explanation:
# A number is even if it is divisible by 2 (remainder 0).
# If the remainder is not 0, the number is odd.

# Asked In Companies:
# Practice Assignment

Num = int(input("Enter the number to check if it's Even or Odd: "))

if Num % 2 == 0:
    print("The number is Even!")
else:
    print("The number is Odd!")