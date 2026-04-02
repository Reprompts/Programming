""" This is a program to check ticket price based on age. """

Age = int(input("Enter the Age of person: "))

Ticket_Price = 100

if Age >= 18 and Age <= 60:
	print(f"The ticket price is {Ticket_Price}")
elif Age > 0 and Age < 18:
	print(f"The ticket price is {Ticket_Price * 0.5} " )
else:
	print("People of this age group are not allowed")
