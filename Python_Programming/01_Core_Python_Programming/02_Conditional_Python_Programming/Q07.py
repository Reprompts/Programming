""" This is a program to check whether a character is a vowel or consonant.
"""

Character = input("Enter the character to check if it's vowel or consonant: ")

if Character in "AEIOUaeiou":
	print("The character is a vowel")
else:
	print("The character is a consonant") 
