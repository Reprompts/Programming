# Question 2: Write a Python program to input all basic data types (int, float, double, char, boolean) and print their values.
# Input:
# int = 10
# float = 5.5
# double = 99.99
# char = A
# boolean = true

# Output:
# 10
# 5.5
# 99.99
# A
# true

# Explanation:
# The program accepts values of different data types and displays them using appropriate variables and print statements.

# Asked In Companies:
# Practice Assignment


Num = eval(input("Enter the Integer value: "))
Float_Num = float(input("Enter the float value: "))
Double_float = float(input("Enter the double value: "))
Char = input("Enter the string value: ")
Bool_value = bool(input("Enter the Boolean value: "))

print(Num)
print(Float_Num)
print(Double_float)
print(Char)
print(Bool_value)