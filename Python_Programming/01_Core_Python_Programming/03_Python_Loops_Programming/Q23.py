"""  Find sum of odd digits in a number.
""" 

Num = int(input("Enter the number to find sum of odd digits: "))

lst = []

while Num:
	Digit = Num % 10
	lst.append(Digit)
	Num = Num // 10

Addition = 0

for i in lst:
	if i % 2 != 0:
		Addition = Addition + i

print(Addition) 

