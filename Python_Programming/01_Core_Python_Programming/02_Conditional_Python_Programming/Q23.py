""" This is a program to calculate electricity bill based on units consumed.
"""

Units = int(input("Enter the amount of units between 0 to 100 consumed: "))

if Units > 90 and Units < 100:
	bill = 1000
elif Units > 50 and Units <= 90:
	bill = 500
elif Units > 10 and Units <= 50:
	bill = 200
elif Units > 0 and Units <= 10:
	bill = 100
else: 
	bill = 0

print(bill) 

