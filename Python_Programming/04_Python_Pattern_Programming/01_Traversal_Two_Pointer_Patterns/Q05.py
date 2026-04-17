"""Count how many even and odd numbers exist in the array"""

arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

ev_count = 0
od_count = 0

for i in arr:
    if i > 0 and i % 2 == 0:
        ev_count += 1
    if i % 2 != 0:
        od_count += 1

print(f"The Even numbers count is {ev_count} & The odd numbers count is {od_count}")