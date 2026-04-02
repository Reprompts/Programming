""" First N odd numbers """ 

N = int(input("Enter the value of N: "))
i = 1

while i != N+1:
	if i % 2 != 0:
		print(i)
	i += 1
