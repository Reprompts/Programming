"""  Write a program to check whether a number is positive and even using nested if.
"""

N = int(input("Enter the number to check whether it's positive and Even: "))

if N % 2 == 0:
	if N > 0:
		print("The number is Even and positive") 

