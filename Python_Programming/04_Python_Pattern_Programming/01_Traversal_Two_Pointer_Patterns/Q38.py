"""Traverse matrix in zig-zag order"""

arr = [[1, 2, 3], 
    [4, 5, 6],
    [7, 8, 9],
    [10, 11, 12]]

rows = len(arr)
cols = len(arr[0])

level = 0 

while level < len(arr):
    for i in range(0, cols):
        print(arr[level][i])
    level += 1
    
    if level < len(arr):
        for i in range(cols-1, -1, -1):
            print(arr[level][i])

    level += 1