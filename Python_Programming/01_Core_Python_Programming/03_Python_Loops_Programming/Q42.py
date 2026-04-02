"""  Calculate sum of squares of first n numbers.
"""

"""  Print numbers which are perfect squares between 1 and 100.
"""

N = int(input("Enter the number here: "))
i = 1
addition = 0

while i * i <= N:
	addition = addition + (i * i)
	i += 1

print(addition)
