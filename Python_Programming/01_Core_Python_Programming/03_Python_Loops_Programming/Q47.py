""" Find product of digits of a number.
"""

N = int(input("Enter the number here: "))
Product = 1

while N:
	Digit = N % 10
	Product *= Digit
	N = N // 10 

print(Product)
