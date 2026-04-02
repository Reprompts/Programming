""" Write a program to check whether a number is divisible by 3 and 5.
"""

N = int(input("Enter a number to check whether it's divisible by 3 and 5: "))

if N % 3 == 0 and N % 5 == 0:
	print("The number is divisible by 3 and 5")

else:
	print("The number is not divisible by 3 and 5")
