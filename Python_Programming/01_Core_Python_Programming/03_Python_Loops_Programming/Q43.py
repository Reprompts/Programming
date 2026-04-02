""" Calculate sum of cubes of first n numbers.
""" 

N = int(input("Enter the number here: "))
i = 1
addition = 0

while i * i * i<= N:
	addition = addition + (i * i * i)
	i += 1

print(addition)