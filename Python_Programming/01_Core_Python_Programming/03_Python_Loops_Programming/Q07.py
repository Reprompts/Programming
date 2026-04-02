""" Calculate factorial of a number using for loop.
"""

Num = int(input("Enter the number to find its factorial: ")) 
fact = 1

for i in range (Num, 0, -1):
	fact = fact * i

print(fact)
