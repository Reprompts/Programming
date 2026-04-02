""" Write a program to print month days using match case.
"""

MN = input("Enter the name of the month: ")

match MN:
	case "January":
		print("Jan has 31 days")
	case "February":
		print("Feb has 28 days for normal years and 29 when it's a leap year")
	case "March":
		print(" Mar has 31 days")
	case "April":
		print("Apr has 30 days")
	case "May":
		print("May has 31 days")
	case "June":
		print("Jun has 30 days")
	case "July":
		print("Jul has 31 days")
	case "August":
		print("Aug has 31 days")
	case "September":
		print("Sep has 30 days")
	case "October":
		print("Oct has 31 days")
	case "November":
		print("Nov has 30 days")
	case "December":
		print("Dec has 31 days")
	case _:
		print("Invalid Month")
