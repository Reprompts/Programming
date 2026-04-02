""" Check whether a number is palindrome.
"""

Num = int(input("Enter the number to check if it's a palindrome: "))

rev_num = 0
original_num = Num

while Num:
	Digit = Num % 10
	rev_num = (rev_num * 10) + Digit
	Num = Num // 10 

if original_num == rev_num:
	print("The number is a palindrome!")
else:
	print("The number is not a palindrome!")

