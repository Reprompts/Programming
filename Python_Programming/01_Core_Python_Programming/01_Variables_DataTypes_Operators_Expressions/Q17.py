# Question 17: Write a Python program to convert seconds into hours, minutes, and seconds.
# Input:
# Seconds = 3665

# Output:
# Hours = 1
# Minutes = 1
# Seconds = 5

# Explanation:
# 1 hour = 3600 seconds.
# 3665 ÷ 3600 gives 1 hour.
# Remaining seconds are converted into minutes and seconds using division and modulus operations.

# Asked In Companies:
# Practice Assignment

Sec = int(input("Enter the amount of seconds: "))

Hours = Sec // 3600
Minutes = (Sec % 3600)// 60
Sec = Sec % 60 

print(f"Hours {Hours}: Minues {Minutes}: Seconds {Sec}")