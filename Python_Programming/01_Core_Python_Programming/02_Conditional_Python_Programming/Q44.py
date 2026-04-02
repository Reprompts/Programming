""" Write a program to check traffic signal actions using match case.
"""

Signal = input("Enter the Signal Red, Orange or Green: ")

match Signal:
	case "Red":
		print("The signal is red stop your vehicles")
	case "Orange":
		print("The signal is about to be red, stop the vehicles slowly")
	case "Green":
		print("The Signal is Green, go ahead")
	case _:
		print("Invalid Signal")
