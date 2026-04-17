"""Find two numbers that sum to target (sorted array)"""

arr = [1,2, 2, 3, 4, 4, 5, 6, 6, 7, 8, 8, 9, 10, 10]
target = 10 
right = len(arr) - 1
left = 0


while left < right:
    if arr[right] + arr[left] == target:
        print(arr[right], arr[left])
        right -= 1
        left += 1
    elif arr[right] + arr[left] > target:
        right -= 1
    elif arr[right] + arr[left] < target:
        left += 1

