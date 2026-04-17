"""Reverse an array in place using a single loop
"""

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]

mid = len(arr) // 2

j = len(arr) - 1

for i in range(0, mid):
    arr[i], arr[j] = arr[j], arr[i]
    j -= 1 

print(arr)

