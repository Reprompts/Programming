""" Write a program to check whether a student passed all subjects. """

Math = int(input("Enter the marks for the math out of 100: "))
Physics = int(input("Enter the marks for the Physics out of 100: "))
English = int(input("Enter the marks for the English out of 100: "))
History = int(input("Enter the marks for the History out of 100: "))

if Math > 40:
	print("You are pass in Maths")
if Physics > 40:
	print("You are pass in Physics")
if English > 40:
	print("You are pass in English")
if History > 40:
	print("You are pass in History")
if Math == Physics == History == English == True:
	print("You are passed in all the subjects")