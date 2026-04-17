"""Check if array is palindrome using reverse traversal"""

arr = [0, 1, 2, 2, 0, 1]
rev = []

for i in range(len(arr)-1, -1, -1):
    rev.append(arr[i])

if arr == rev:
    print("It's a palindrome!")
else:
    print("It's not a palindrome!")

    