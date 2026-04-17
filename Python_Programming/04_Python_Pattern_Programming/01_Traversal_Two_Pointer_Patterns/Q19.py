"""Count number of peaks"""

arr = [7, 5, 2, 4, 2, 3, 4, 5, 45, 7, 8, 9, 15, 22, 21, 27, 22]

count = 0

for i in range(1, len(arr)-1):
    if arr[i-1] < arr[i] and arr[i] > arr[i+1]:
        print(arr[i-1], arr[i], arr[i+1])
        count += 1

print(count)