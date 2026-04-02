"""  This is a program to check salary bonus based on years of service.
"""

Experience = int(input("Enter the Experience in Years: "))
Salary = int(input("Enter the Salary: "))

if Experience < 2:
	print(f"The bonus for you is {Salary * (1/20)}")
elif Experience > 2 and Experience < 5:
	print(f"The bonus for you is {Salary * (1/10)}")
elif Experience >=5 and Experience <= 10:
	print(f"The bonus for you is {Salary * (1/5)}")
elif Experience > 10:
	print(f"The bonus for you is {Salary * (1/4)}")
else:
	print("Invalid Experience")


