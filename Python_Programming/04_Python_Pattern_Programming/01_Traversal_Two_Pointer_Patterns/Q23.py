"""Check if array is palindrome using two pointers"""


arr = [1, 2, 3, 4, 5, 4, 3, 2, 1]

print(arr)
original_arr = arr
mid = len(arr) // 2
j = len(arr) - 1

for i in range(0, mid):
    arr[i], arr[j] = arr[j], arr[i]
    j -= 1

print(arr)

if original_arr == arr:
    print("The array is palindrome!")
else:
    print("The array is not a palindrome!")