"""Remove duplicates from sorted array using two pointers"""

arr = [1,2, 2, 3, 4, 4, 5, 6, 6, 7, 8, 8, 9, 10, 10]

count = 1

for i in range(2, len(arr)):
    if arr[i] != arr[count-1]:
        arr[count] = arr[i]
        count += 1

print(arr[:count])