"""Find the first element greater than K"""

arr = [0, 1, 2, 2, 2, 3, 4, 5, 6, 7, 8, 9, 15, 21, 21, 27, 27]

k = int(input("Enter the number k here: "))

for i in arr:
    if k < i:
        print(i)
        break 
