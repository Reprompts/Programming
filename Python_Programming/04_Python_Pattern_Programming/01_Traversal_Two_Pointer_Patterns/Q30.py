"""Find intersection of two sorted arrays"""

arr1 = [1, 2, 3, 9, 10, 14]
arr2 = [1, 8, 9 , 10, 12, 13, 14, 15]

pointa = 0
pointb = 0

while pointa < len(arr1) and pointb < len(arr2):
    if arr1[pointa] < arr2[pointb]:
        pointa += 1
    elif arr1[pointa] > arr2[pointb]:
        pointb += 1
    elif arr1[pointa] == arr2[pointb]:
        print(arr1[pointa], arr2[pointb])
        pointa += 1
        pointb += 1

