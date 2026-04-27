# Logical Operators in Python
# Logical Operators are used to combine conditional statements. They return a boolean value (True or False) based on the combination of the conditions. The logical operators in Python are:
# Operator	Description
# and	Returns True if both statements are true
# or	Returns True if at least one statement is true
# not	Returns True if the statement is false

# Input two numbers from user and check if they are positive and even using logical operators
num1 = int(input("Enter first number : "))
num2 = int(input("Enter second number : "))

print("Both numbers are positive and even : ", (num1 > 0 and num1 % 2 == 0) and (num2 > 0 and num2 % 2 == 0))
print("At least one number is positive and even : ", (num1 > 0 and num1 % 2 == 0) or (num2 > 0 and num2 % 2 == 0))
print("Neither number is positive and even : ", not ((num1 > 0 and num1 % 2 == 0) or (num2 > 0 and num2 % 2 == 0)))