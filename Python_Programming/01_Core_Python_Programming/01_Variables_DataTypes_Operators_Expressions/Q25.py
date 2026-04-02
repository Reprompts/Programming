# Question 25: Write a Python program to check whether a number is palindrome or not.
# Input:
# 121

# Output:
# Palindrome

# Explanation:
# A palindrome number remains the same when reversed.
# Since 121 reversed is also 121, it is a palindrome.

# Asked In Companies:
# Practice Assignment

Num = int(input("Enter the number to find if it's a palindrome: "))
rev_num = 0
temp=Num

while Num>0:
    digit = Num  % 10
    Num = Num // 10
    rev_num = (rev_num*10)+digit
    

if rev_num==temp:
    print("The given number is a palindrome!")
else:
    print("The given number is not a palindrome!")

