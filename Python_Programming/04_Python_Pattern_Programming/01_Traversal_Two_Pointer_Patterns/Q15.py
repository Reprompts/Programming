"""Print elements from the last even index to the beginning"""

arr = [0, 1, 2, 2, 2, 3, 4, 5, 6, 7, 8, 9, 15, 21, 21, 27, 27]

for i in range(len(arr)-1, -1, -1):
    if i % 2 == 0:
        print(arr[i])
        