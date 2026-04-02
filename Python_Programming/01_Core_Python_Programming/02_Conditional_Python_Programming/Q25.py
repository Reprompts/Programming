"""  Write a program to check whether a triangle is equilateral, isosceles, or scalene.
""" 

A = int(input("Enter the length of side 1: "))
B = int(input("Enter the length of side 2: "))
C = int(input("Enter the length of side 3: "))

if A != B and B != C and C != A:
	print("This is a scelene triangle!")
elif A == B and B == C and A == C:
	print("This is an equilateral triangle!")
else:
	print("This is an isoscelene triangle!")

