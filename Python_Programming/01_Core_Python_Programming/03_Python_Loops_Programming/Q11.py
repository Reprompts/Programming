""" Count number of digits in a number.
"""

Num = input("Enter the number to find its length: ") 
Digit_count = 0

for i in Num:
	Digit_count += 1

print("The count of digits in number is: ", Digit_count)