""" Write a program to build a simple ATM menu using match case.
""" 

print("Type 1 for Deposit: ")
print("Type 2 for Balance Check: ")
print("Type 3 for Witdrawl: ")
print("Type 4 for Exit: ")

Balance = 0

while 1:
	Option = int(input("Eter your option here, and Enter 4 for exiting: "))
	match Option:
		case 1:
			Deposit = int(input("Enter your Deposit amount: "))
			Balance += Deposit
		case 2:
			print("Your current balance is: ", Balance)
		case 3: 
			Withdraw = int(input("Enter the amount you want to withdraw: "))
			Balance -= Withdraw
		case 4:
			print("Thank you for visiting")
			break
		case _:
			print("Invalid Input")

