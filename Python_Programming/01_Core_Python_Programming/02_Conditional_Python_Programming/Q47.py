""" Write a program to check user role (admin, user, guest) using match case.
"""

Role = input("Eter your role: ")

match Role:
	case "Admin":
		print("You will have admin level access")
	case "User":
		print("You will have user level access")
	case "Guest":
		print("You will have Guest level access")
	case _:
		print("Invalid Input")
