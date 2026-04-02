""" This is a program to check whether a given character is uppercase or lowercase. """ 

# The ASCII value of A is 65 and of Z is 90, The ASCII value of a is 97 and of z is 122

Character = input("Enter the character to check whether it's Uppercase or Lowercase: ")

if ord(Character) > 64 and ord(Character) < 91:
	print("The character is Uppercase")
elif ord(Character) > 96 and ord(Character) < 123:
	print("The character is Lowercase")
else:
	print("The input is invalid")

