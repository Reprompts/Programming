"""Find the minimum element in an array"""

arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
L = len(arr)
min = arr[0]

for i in range(1, L):
    if min > arr[i]:
        min = arr[i]

print(min)