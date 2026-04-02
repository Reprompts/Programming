""" Write a program to check whether a person can apply for a loan.
"""

EL = int(input("Enter the existing loan amount you are due pay: "))
conf = input("Type Yes if your income is above 50000 otherwise type No: ")

if EL > 100000 and conf == "No":
	print("You are not eligible for the loan as you have too much of loan already!")

else:
	print("You are Eligible for the loan, you can apply!") 

