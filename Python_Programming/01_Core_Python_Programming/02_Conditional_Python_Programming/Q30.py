"""  Write a program to check the type of number (single, double, or three digit).
"""

N = int(input("Enter a number to check how many digits it has: "))

if N % 10 == N:
	print("This is a single digit number: ")
elif N % 100 == N:
	print("This is a 2 digit number: ")
elif N % 1000 == N:
	print("This is a 3 digit number: ")
else:
	print("Enter a proper number") 

