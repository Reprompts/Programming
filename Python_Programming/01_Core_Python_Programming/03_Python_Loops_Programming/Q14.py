""" Print Fibonacci series up to n terms.
"""

N = int(input("Enter the N number: ")) 

x, y = 0, 1
fab = 0

for i in range (0, N-1):
	fab = x + y
	print(fab, end=" ")
	x = y
	y = fab

	
	
	