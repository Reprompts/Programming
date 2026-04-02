# Question 11: Write a Python program to enter marks of five subjects and calculate total marks and percentage.
# Input:
# Marks = 70, 75, 80, 65, 60

# Output:
# Total = 350
# Percentage = 70%

# Explanation:
# Total marks are calculated by adding all five subject marks.
# Percentage = Total ÷ 5.

# Asked In Companies:
# Practice Assignment

Sub1 = int(input("Enter the marks for Sub1: "))
Sub2 = int(input("Enter the marks for Sub2: "))
Sub3 = int(input("Enter the marks for Sub3: "))
Sub4 = int(input("Enter the marks for Sub4: "))
Sub5 = int(input("Enter the marks for Sub5: "))

total_marks = Sub1 + Sub2 + Sub3 + Sub4 + Sub5
percentage = ((total_marks / 5) * 100)/ 100

print("The Total marks of the student are:", total_marks)
print("The Percentage of the student is: ", percentage)


