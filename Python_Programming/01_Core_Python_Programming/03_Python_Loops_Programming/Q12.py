""" Reverse a number using while loop.
"""

Num = int(input("Enter the number to be reversed: "))
temp = 0
rev_num = 0

while Num:
	Digit = Num % 10
	rev_num = (rev_num * 10) + Digit
	Num = Num // 10 

print(rev_num) 