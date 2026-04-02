""" Find sum of digits of a number.
"""

Num = int(input("Enter the number to find sum of its digits: ")) 
addition = 0

while Num:
	digit = Num % 10
	addition += digit
	Num = Num // 10

print("The addition of the digits of the number is: ", addition)
