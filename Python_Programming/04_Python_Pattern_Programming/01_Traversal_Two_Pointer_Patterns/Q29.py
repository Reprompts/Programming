"""Merge two sorted arrays using traversal"""

arr1 = [1, 2, 3, 9, 10]
arr2 = [7, 8, 12, 13, 14, 15]
merged = []

pointa = 0
pointb = 0

while pointa < len(arr1) and pointb < len(arr2):
    if arr1[pointa] < arr2[pointb]:
        merged.append(arr1[pointa])
        pointa += 1
    elif arr1[pointa] > arr2[pointb]:
        merged.append(arr2[pointb])
        pointb += 1

merged.extend(arr1[pointa:])
merged.extend(arr2[pointb:])


print(merged)




