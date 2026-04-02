""" Program to check Armstrong Number """

Num = int(input("Enter the number to check if it's Armstrong: ")) 
temp = Num
count = 0
lst = []
arm = 0
while Num:
	Digit = Num % 10
	lst.append(Digit)
	count = count + 1
	Num = Num // 10

for i in lst:
	arm = arm + (i ** count)

if arm == temp:
	print("This is an Armstrong Number!")
else:
	print("This is not an Armstrong Number!")
