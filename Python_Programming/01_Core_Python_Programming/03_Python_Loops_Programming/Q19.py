"""  Check whether a number is prime """ 
num = int(input("Enter a number to check if it's prime: "))

for i in range (2, num):
	if num % i == 0:
		is_prime = False
		break
	else:
		is_prime = True

if is_prime:
	print("The number is prime") 
else:
	print("The number is not prime") 


