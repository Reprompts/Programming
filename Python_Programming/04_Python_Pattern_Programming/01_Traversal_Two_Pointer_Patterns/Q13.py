"""Find the last occurrence of an element"""

arr = [0, 1, 2, 2, 2, 3, 4, 5, 6, 7, 8, 9, 15, 21, 21, 27, 27]
el = int(input("Enter the element you want to find last occurence of: "))

for i in range(len(arr)-1, -1, -1):
    if el == arr[i]:
        print(i)
        break
