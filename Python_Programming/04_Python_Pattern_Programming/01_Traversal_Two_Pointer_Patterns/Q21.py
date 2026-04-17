"""Find the largest difference between adjacent elements"""

arr = [7, 5, 2, 4, 2, 3, 4, 5, 45, 7, 8, 9, 15, 22, 21, 27, 22]
diff = []

for i in range(1, len(arr)):
    diff.append(arr[i] - arr[i-1])

print(max(diff))