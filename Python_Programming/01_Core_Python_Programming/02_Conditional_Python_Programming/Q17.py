""" This is a program to check grade based on marks (A, B, C, Fail).
""" 

Marks = int(input("Enter the marks of student: "))

if Marks >= 80 and Marks <= 100:
	print("The grade of student is A")
elif Marks >= 70 and Marks < 80:
	print("The grade of student is B")
elif Marks >= 40 and Marks < 70:
	print("The grade of student is C")
else:
	print("The student is failed")

 