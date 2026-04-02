""" Write a program to check whether a number is greater than 0 and less than 100.
"""

Num = int(input("Enter a number to check whether it comes in between 0 and 100: "))

if Num > 0 and Num < 101:
	print("The number is between 0 and 100")
else:
	print("The number is not between 0 and 100")
