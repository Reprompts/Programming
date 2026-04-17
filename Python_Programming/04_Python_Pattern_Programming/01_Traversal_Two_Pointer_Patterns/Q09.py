"""Print indices of all occurrences of a target element"""

N = int(input("Enter the number for which you want to find the indices where it occured: "))
arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 15, 21, 27, 2, 2, 27, 21]

for i in range(0, len(arr)):
    if N == arr[i]:
        print(i)
