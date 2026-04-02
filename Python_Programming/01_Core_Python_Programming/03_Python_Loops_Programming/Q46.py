""" Print first n multiples of a number.
""" 

N = int(input("Enter the N here: "))
num = int(input("Enter the Number here: "))

for i in range(1, N + 1):
	print(num * i)

