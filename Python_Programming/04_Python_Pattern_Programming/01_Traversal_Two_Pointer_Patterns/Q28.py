"""Count pairs with sum less than target"""

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 10
left = 0 
right = len(arr) - 1

while left < right:
    if arr[left] + arr[right] < target:
        print(arr[left], arr[right])
        left += 1
    elif arr[left] + arr[right] >= target:
        right -= 1 




