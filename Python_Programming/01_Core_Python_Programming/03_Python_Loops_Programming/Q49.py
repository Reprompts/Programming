"""  Display menu-driven program using while loop.
"""

print("1 for Task A: ")
print("2 for Task B: ")
print("3 for Task C: ")
print("4 for Task D: ")
print("5 for Exiting: ")



while 1:
	Option = int(input("Enter your option here: "))

	if Option == 1:
		print("Performing Task A right now")
	elif Option == 2:
		print("performing Task B right now")
	elif Option == 3:
		print("Performing Task C right now")
	elif Option == 4: 
		print("Performing Task D right now")
	elif Option == 5:
		print("Thanks for Using the machine")
		break
	else:
		print("Invalid Input")


