""" This is a program to check whether a given year is a leap year or not. """

Year = int(input("Enter the Year to check if it's a leap year: ")) 

if (Year % 4 == 0 and Year % 100 != 0) or Year % 400 == 0:
	print("The year is a leap year") 
else:
	print("The year is not leap year")

