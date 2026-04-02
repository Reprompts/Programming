""" This is a program to find the greatest of three numbers.
"""

A = int(input("Enter the number A: "))
B = int(input("Enter the number B: "))
C = int(input("Enter the number C: "))

if A > B and A > C:
	print("A is the greatest")
elif B > A and B > C:
	print("B is the greatest")
elif C > A and C > B:
	print("C is the greatest")
else:
	print("Invalid Input")
