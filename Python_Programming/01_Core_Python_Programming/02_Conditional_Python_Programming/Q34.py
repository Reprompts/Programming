""" Write a program to check whether a year is a leap year and century year.
"""

Year = int(input("Enter the year here: "))

if Year % 4 == 0 and Year % 400 ==0 and Year % 100 != 0:
	print("This is a leap year: ")
elif Year % 100 ==0 and Year % 400 != 0:
	print("This is a century year")
else:
	print("Invalid Input")

