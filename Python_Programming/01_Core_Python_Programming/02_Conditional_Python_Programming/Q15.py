"""  This is a program to check whether a number is divisible by both 3 and 7 or not. """

Num = int(input("Enter a number to check whether it's divisible by 3 and 7: "))

if Num % 3 == 0 and Num % 7 == 0:
	print("The number is divisible by 3 and 7")
else:
	print("The number is not divisible by 3 and 7")

