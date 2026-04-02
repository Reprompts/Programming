""" This is a program to check whether a person is eligible to vote or not. """

Age = int(input("Enter the age of person: ")) 

if Age >= 18 and Age <= 100:
	print("The person is eligible for voting")
elif Age < 18:
	print("The person is not eligible for voting") 
else:
	print("Invalid input!") 