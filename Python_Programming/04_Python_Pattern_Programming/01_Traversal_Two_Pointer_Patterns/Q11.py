"""Print all elements except duplicates (skip repeating adjacent elements in sorted array)"""

arr = [0, 1, 2, 2, 2, 3, 4, 5, 6, 7, 8, 9, 15, 21, 21, 27, 27]

for i in range(0, len(arr)):
    if arr[i] == arr[i-1]:
        continue
    print(arr[i])
