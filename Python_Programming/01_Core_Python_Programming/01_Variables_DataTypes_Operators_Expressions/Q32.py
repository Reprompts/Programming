# Question 32: Write a Python program to check whether a triangle is valid or not using its three angles.
# Input:
# Angle1 = 60
# Angle2 = 60
# Angle3 = 60

# Output:
# Valid Triangle

# Explanation:
# A triangle is valid only if the sum of all three angles is exactly 180°.
# 60 + 60 + 60 = 180, so it is valid.

# Asked In Companies:
# Practice Assignment

Angle1 = int(input("Enter the Angle 1: "))
Angle2 = int(input("Enter the Angle 2: "))
Angle3 = int(input("Enter the Angle 3: "))

if Angle1 + Angle2 + Angle3 == 180:
    print("This is a triangle!")
else:
    print("This is not a triangle!")