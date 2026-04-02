""" Write a program to check login status based on username and password.
"""

Username = input("Enter the Username here: ")
Password = input("Enter the Password here: ")

if Username == "Admin":
	if Password == "Pass":
		print("You have Logged in successfully!")
	else:
		print("Wrong Password")
else:
	print("Wrong Username")

