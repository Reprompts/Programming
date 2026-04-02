""" Find sum of numbers entered by user until 0 is entered. """


while 1:
	option = int(input("Enter 1 for the addition or 0 for exit: "))

	if option == 1:
		A = int(input("Enter the value of Number 1: "))
		B = int(input("Enter the value of Number 2: "))
		print(A + B)
	elif option == 0:
		print("Thanks for visiting the adder!")
		break
	else:
		print("Invalid Option is selected!")


