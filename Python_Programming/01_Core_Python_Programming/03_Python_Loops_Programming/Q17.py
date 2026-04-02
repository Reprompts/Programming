""" Find largest digit in a number.
"""

Num = int(input("Enter the Number to find the largest digit in it: ")) 
lst = [] 

while Num:
	Digit = Num % 10
	lst.append(Digit)
	Num = Num // 10 

count = 0

print(max(lst))
