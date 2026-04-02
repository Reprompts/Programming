# Question 29: Write a Python program to find quotient and remainder using arithmetic operators.
# Input:
# Dividend = 20
# Divisor = 3

# Output:
# Quotient = 6
# Remainder = 2

# Explanation:
# The division operator (/) gives the quotient.
# The modulus operator (%) gives the remainder.

# Asked In Companies:
# Practice Assignment

Dividend = int(input("Enter the value of Dividend: "))
Divisor = int(input("Enter the value of Divisor: "))

Quotient = int(Dividend/Divisor)
Remainder = Dividend % Divisor

print(f"The Quotiet is: {Quotient}, The Remainder is: {Remainder}")
