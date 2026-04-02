""" Count total words in a string.
"""

String = input("Enter a string to find number of words in it: ")

words = 0



for i in String:
	if i == ' ':
		words = words + 1

print(words + 1)
		