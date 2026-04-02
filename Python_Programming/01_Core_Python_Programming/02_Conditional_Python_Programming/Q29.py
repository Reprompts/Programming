""" Write a program to check blood donation eligibility based on age and weight.
"""

Age = int(input("Enter your age for donation: "))
Weight = int(input("Enter your Weight in Kg for donation: "))

if Age > 18 and Weight > 50:
	print("You are eligible for the donation")
else:
	print("You are not eligible for the donation") 

