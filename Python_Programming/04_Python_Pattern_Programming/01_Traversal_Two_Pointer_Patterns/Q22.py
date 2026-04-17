"""Reverse an array using two pointers"""

arr = [7, 5, 2, 4, 2, 3, 4, 5, 45, 7, 8, 9, 15, 22, 21, 27, 22]

print(arr)
mid = len(arr) // 2
j = len(arr) - 1

for i in range(0, mid):
    arr[i], arr[j] = arr[j], arr[i]
    j -= 1

print(arr)