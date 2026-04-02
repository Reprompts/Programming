# Question 9: Write a Python program to enter two angles of a triangle and find the third angle.
# Input:
# Angle1 = 50
# Angle2 = 60

# Output:
# Third Angle = 70

# Explanation:
# The sum of all angles in a triangle is 180°.
# Third Angle = 180 ? (Angle1 + Angle2).

# Asked In Companies:
# Practice Assignment

Angle1 = float(input("Enter the degree of angle1: "))
Angle2 = float(input("Enter the degree of angle2: "))

Angle3 = 180 - (Angle1 + Angle2)

print("The degree of the third angle is: ", Angle3)
