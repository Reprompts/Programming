""" Check whether number is strong number.
"""

N = int(input("Enter the number here: "))
Addition = 0
Product = 1
lst = []
while N:
	Digit = N % 10
	lst.append(Digit)
	N = N // 10

for i in lst:
	for j in range(1, i + 1):
		Product = Product * j
	Addition += Product

print(Addition)