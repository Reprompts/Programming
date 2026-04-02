"""  Write a program to check whether a person is eligible for driving license.
"""

Age = int(input("Enter the age of the driver to check if he is eligible for the license: "))

if Age > 18 and Age < 70:
	print("The driver is eligible for the license")
else:
	print("The driver is not eligible for the license")

