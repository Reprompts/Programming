"""  Print numbers until user enters a negative number.
"""

while 1:
	option = int(input("Enter 1 for the addition or 0 for exit: "))

	if option >= 0:
		A = int(input("Enter the value to print: "))
		print(A)
	elif option < 0:
		print("Thanks for visiting the printer!")
		break
	else:
		print("Invalid Option is selected!")

