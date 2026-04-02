"""  Count vowels in a string.
"""

String = input("Enter the string to check how many vowels it contains: ")

count = 0

for i in String:
	if i in "aeiouAEIOU":
		count = count + 1

print(count)