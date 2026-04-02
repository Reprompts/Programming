""" Print alternate characters of a string.
"""

S = input("Enter the string here: ")
L = len(S)

for i in range(0, L, 2):
	print(S[i])

