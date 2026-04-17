"""Find sum of each column"""

arr = [[1, 2, 3, 4], [5, 6, 7, 8]]

rows = len(arr)
cols = len(arr[0])

for j in range(cols):
    addition = 0
    for i in range(rows):
        addition += arr[i][j]
    print(f"The addition for column {j} is {addition}") 

    