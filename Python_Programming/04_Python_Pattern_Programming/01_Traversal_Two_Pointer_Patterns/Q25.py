"""Partition array into negatives and positives""" 

arr = [ -1, 1, -2, 2, 3, 4, 5, -4, -8, 8, 10]
count = 0

for i in range(0, len(arr)):
    if arr[i] < 0:
        arr[count], arr[i] = arr[i], arr[count]
        count += 1

print(arr)