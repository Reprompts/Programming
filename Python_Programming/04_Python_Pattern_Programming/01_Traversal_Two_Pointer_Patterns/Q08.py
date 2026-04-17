"""Count elements divisible by 3 but not by 5"""

arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 15, 21, 27]

for i in arr:
    if i % 3 == 0 and i % 5 != 0:
        print(i)
        

