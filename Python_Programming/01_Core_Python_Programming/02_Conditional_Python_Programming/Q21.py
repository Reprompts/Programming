""" Write a program to find the smallest of three numbers.
""" 

A = int(input("Enter the Number A: "))
B = int(input("Enter the Number B: "))
C = int(input("Enter the Number C: "))

if A < B and A < C:
	print("A is the smallest")
elif B < A and B < C:
	print("B is the smallest")
else: 
	print("C is the smallest") 


	
