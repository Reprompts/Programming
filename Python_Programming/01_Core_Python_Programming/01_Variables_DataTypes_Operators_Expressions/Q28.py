# Question 28: Write a Python program to calculate the net salary of an employee.
# Input:
# Basic = 20000
# HRA = 10%
# DA = 5%
# Tax = 2%

# Output:
# Net Salary = 22600

# Explanation:
# HRA and DA are calculated as percentages of the basic salary and added to it.
# Tax is deducted after adding allowances to compute the final net salary.

# Asked In Companies:
# Practice Assignment



Salary = int(input("Enter the basic salary of an employee: "))

hra = Salary * (10/100)
da = Salary * (5/100)

print("The complete Salary of the Employee is: ", Salary + hra + da)

print("The Net Salary after Tax deduction is: ", Salary - ((Salary + hra + da) * 2/100))