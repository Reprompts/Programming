# Question 18: Write a Python program to convert days into years, months, and weeks.
# Input:
# Days = 400

# Output:
# Years = 1
# Months = 1
# Weeks = 1

# Explanation:
# 1 year = 365 days.
# After subtracting 365 days, the remaining days are divided into months (30 days each) and weeks (7 days each).

# Asked In Companies:
# Practice Assignment

D = int(input("Enter the number of days: "))

Y = D // 365 
M = (D % 365) // 30 
D = D % 365

print(D, M, Y, sep=" - ")