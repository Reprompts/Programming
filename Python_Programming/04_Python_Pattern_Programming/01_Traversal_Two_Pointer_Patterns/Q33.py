"""Print matrix column-wise"""

arr = [[1, 2, 3, 4], [5, 6, 7, 8]]

rows = len(arr)
cols = len(arr[0])

for j in range(cols):
    for i in range(rows):
        print(arr[i][j], end=" ")
    print()

