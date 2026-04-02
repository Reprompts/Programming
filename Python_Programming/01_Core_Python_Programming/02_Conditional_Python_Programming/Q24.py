"""  Write a program to check exam result (Distinction, First Class, Pass, Fail).
"""

Result = int(input("Enter the marks you have got: "))

if Result < 40:
	print("You've failed in exam")
elif Result >= 40 and Result <75:
	print("You are First Class pass")
elif Result > 75 and Result <= 100:
	print("You have passed the exam with distinction!")
else:
	print("Invalid marks are entered")
