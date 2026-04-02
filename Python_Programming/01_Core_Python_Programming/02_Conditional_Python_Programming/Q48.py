""" Write a program to print language choice using match case.
""" 

print("Type 1 for Marathi: ")
print("Type 2 for Hindi: ")
print("Type 3 for English: ")
print("Type 4 for Mandarin: ")

while 1:
	Option = int(input("Eter your option here, and Enter 5 for exiting: "))
	match Option:
		case 1:
			print("You can speak in Marathi now")
		case 2:
			print("You can speak in Hindi now")
		case 3: 
			print("You can speak in English now")
		case 4: 
			print("You can speak in Mandarin now")
		case 5:
			print("Thank you for visiting")
			break
		case _:
			print("Invalid Input")

			