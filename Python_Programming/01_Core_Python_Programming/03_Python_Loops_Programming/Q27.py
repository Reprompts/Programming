"""  Print all factors of a number.
""" 

A = int(input("Enter a number to find its factors: ")) 

for i in range (1, A+1):
	if A % i == 0:
		print(i) 

