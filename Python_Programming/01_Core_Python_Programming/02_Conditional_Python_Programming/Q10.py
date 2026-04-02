"""  This is a program to check whether a number is a single-digit number or not. """

Num = int(input("Enter the number to check if it's single digit or not: "))

if Num > -10 and Num < 10:
	print("The number is single digit")
else:
	print("The number is not single digit")

