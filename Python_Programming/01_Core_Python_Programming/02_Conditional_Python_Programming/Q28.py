""" Write a program to calculate discount based on total shopping amount.
"""

Amount = int(input("Enter the shopping amount: "))

if Amount > 30000:
	print("Your total discount value is: ", Amount * 0.05)
else:
	print("Spend more than 30000 to get discount")

