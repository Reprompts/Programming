"""  Calculate power of a number without using pow().
"""

Num = int(input("Enter the number to find it's Power: "))
power = int(input("Enter the value of power: "))

expo = 1

for i in range(1, power+1):
	expo = expo * Num

print(expo) 


	