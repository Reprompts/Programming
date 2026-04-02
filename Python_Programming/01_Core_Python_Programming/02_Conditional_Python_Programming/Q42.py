""" Write a program to perform calculator operations using match case.
"""

print("Enter 1 for Addition \nEnter 2 for Subtraction \nEnter 3 for Multiplication \nEnter 4 for Division \nEnter 5 for Exit: ")

while 1:
	Option = int(input("Eter the option here: "))
	A = int(input("Enter the number A: "))
	B = int(input("Enter the number B: "))
	
	match Option:
		case 1:
			print("The Addition is : ", A + B)
		case 2:
			print("The Subtraction is :", A - B)
		case 3:
			print("The Multiplication is: ", A * B)
		case 4:
			print("The Division is: ", A / B)
		case 5:
			print("Thanks for using the calculator")
			break
		case _:
			print("Invalid Input")
		