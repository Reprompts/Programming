""" Count consonants in a string.
"""


String = input("Enter the string to check how many consonants it contains: ")

count = 0

for i in String:
	if i not in "aeiouAEIOU \n":
		count = count + 1

print(count)