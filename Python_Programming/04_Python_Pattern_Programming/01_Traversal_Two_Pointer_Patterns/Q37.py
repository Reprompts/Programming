"""Print matrix in spiral order"""


arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

rows = len(arr)
cols = len(arr[0])

top = 0
left = 0
bottom = rows
right = cols

while top < bottom and left < right:
    for i in range(left, right):
        print(arr[top][i])
    
    top += 1

    for i in range(top, bottom):
        print(arr[i][right-1])

    right -= 1 

    if left < right:
        for i in range(right-1, left-1, -1):
            print(arr[bottom-1][i])
    
    bottom -= 1
    
    if top < bottom:
        for i in range(bottom-1, top-1, -1):
            print(arr[i][left])
            
    left += 1 

