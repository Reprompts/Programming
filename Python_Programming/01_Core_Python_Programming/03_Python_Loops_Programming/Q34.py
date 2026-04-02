""" Check whether a string is palindrome.
"""

String = input("Enter a string to reverse it: ")
rev = ""

for i in String:
	rev = i + rev

if String == rev:
	print("The entered string is a palindrome!")
else:
	print("The entered string is not a palindrome!")

