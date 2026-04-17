"""Find first increasing pair (arr[i] < arr[i+1])"""

arr = [7, 5, 2, 2, 2, 3, 4, 5, 6, 7, 8, 9, 15, 21, 21, 27, 27]

for i in range(1, len(arr)):
    if arr[i-1] < arr[i]:
        print(arr[i-1], arr[i])
        break