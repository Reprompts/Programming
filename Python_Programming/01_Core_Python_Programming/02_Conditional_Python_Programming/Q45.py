""" Write a program to print menu-based food selection using match case.
"""

print("Enter 1 for the coffee: ")
print("Enter 2 for the Chai: ")
print("Enter 3 for Upma: ")
print("Enter 4 for Juice: ")
print("Enter 5 for exiting: ")

while 1:
	Option = int(input("Enter the option to select food item: "))
	match Option:
		case 1:
			print("Your order for coffee has been taken")
		case 2:
			print("Your order for Chai has been taken")
		case 3:
			print("Your order for Upma has been taken")
		case 4:
			print("Your order for Juice has been taken")
		case 5:
			print("Thanks for the visit")
			break
		case _:
			print("Invalid Input")
