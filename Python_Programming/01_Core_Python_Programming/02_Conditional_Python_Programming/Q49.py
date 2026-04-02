""" . Write a program to print result status using match case.
"""

result = int(input("Enter your result here: "))

if result < 40:
	op = "F"
elif result >= 40 and result < 60:
	op = "C"
elif result >= 60 and result < 80:
	op = "B"
elif result >= 80 and result <= 100:
	op = "A"
else:
	print("Invalid Input")
	op = "D"

match op:		
		
	case "F":
		print("You are falied in exam")
		
	case "C":
		print("You have got C grade")
	case "B":
		print("You have got B grade")
	case "A":
		print("You have got A grade")
	case _:
		print("Enter the valid marks")


