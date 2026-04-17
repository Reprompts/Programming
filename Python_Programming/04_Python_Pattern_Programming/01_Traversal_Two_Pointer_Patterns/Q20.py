"""Replace every element with difference from next element"""

arr = [7, 5, 2, 4, 2, 3, 4, 5, 45, 7, 8, 9, 15, 22, 21, 27, 22]

for i in range(1, len(arr)):
    arr[i-1] = arr[i] - arr[i-1]

print(arr)