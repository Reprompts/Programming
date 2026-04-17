"""Count number of adjacent equal pairs"""

arr = [0, 1, 2, 2, 2, 3, 4, 5, 6, 7, 8, 9, 15, 21, 21, 27, 27]

count = 0

for i in range(1, len(arr)):
    if arr[i-1] == arr[i]:
        count += 1

print(f"The count of equal adjacent paris is {count}")