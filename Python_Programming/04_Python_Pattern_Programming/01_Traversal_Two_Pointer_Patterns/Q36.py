"""Print main diagonal and secondary diagonal"""

arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

rows = 3
cols = 3

for i in range(rows):
    print(arr[i][i])

for i in range(rows):
    print(arr[i][cols - 1 - i])

