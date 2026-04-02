""" Find smallest digit in a number. """

Num = int(input("Enter the number to find the smallest digit in it: "))
lst = []

while Num:
	Digit = Num % 10
	lst.append(Digit)
	Num = Num // 10

print(min(lst))
