""" Write a program to print grade description using match case.
"""

grade = input("Enter grade A, B or C for its description: ")

match grade:
	case "A":
		print("This is A grade it's the best quality product")
	case "B":
		print("This is B grade medium quality product")
	case "C":
		print("This is C grade lower quality product")
	case _:
		print("Invalid Input")
