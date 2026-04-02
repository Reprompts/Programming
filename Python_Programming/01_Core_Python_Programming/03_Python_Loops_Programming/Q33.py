""" Print reverse of a string.
"""

String = input("Enter a string to reverse it: ")
rev = ""

for i in String:
	rev = i + rev

print(rev)