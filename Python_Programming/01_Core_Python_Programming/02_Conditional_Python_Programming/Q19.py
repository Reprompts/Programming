"""  This is a program to print the day name based on day number (1–7).
"""

Day_Num = int(input("Enter the Day Number to check the Day: "))

match Day_Num:
	case 1:
		print("The day is Monday")
	case 2:
		print("The day is Tuesday")
	case 3:
		print("The day is Wednesday")
	case 4:
		print("The day is Thursday")
	case 5:
		print("The day is Friday")
	case 6:
		print("The day is Saturday")
	case 7:
		print("The day is Sunday")

	case _:
		print("Invalid Input") 



