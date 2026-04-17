"""Find sum of each row"""

arr = [[1, 2, 3, 4], [5, 6, 7, 8]]

rows = len(arr)
cols = len(arr[0])


for i in range(rows):
    addition = 0
    for j in range(cols):
        addition = addition + arr[i][j]
    print(f"Addition for the row {i} is {addition}")
