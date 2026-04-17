"""Find missing number in sorted array"""

arr = [1, 2, 4, 5, 6, 7, 8, 9, 10]

for i in range(1, len(arr)-1):
    if arr[i] - arr[i-1] == 1:
        continue 
    else:
        print(arr[i] - 1)