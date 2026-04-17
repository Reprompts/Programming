"""Print all elements greater than a given number K"""

k = int(input("Enter the number K: "))
arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

for i in arr: 
    if i > k:
        print(i)
