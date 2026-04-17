"""Find the maximum element in an array"""

arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
L = len(arr)
max = arr[0]

for i in range(1, L):
    if max < arr[i]:
        max = arr[i]

print(max)