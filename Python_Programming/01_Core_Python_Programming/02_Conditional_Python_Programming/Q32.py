""" Write a program to check whether a student is eligible for exam (attendance + marks).
"""

At = int(input("Enter the attendance in percentage here: "))
marks = int(input("Enter the marks in percentage here: "))

if At > 80:
	if marks > 60:
		print("You are eligible for the exam")

