# WAP to check if a number entered by the user is even or odd.
num = int(input("Enter a number: "))
if num % 2 == 0:
    print(f"{num} is an even number.")
else:    
    print(f"{num} is an odd number.")



# wap TO find the greatest of 3 numbers entered by the user.
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

if num1 >= num2 and num1 >= num3:
    greatest = num1
elif num2 >= num1 and num2 >= num3:
    greatest = num2
else:
    greatest = num3

print(f"The greatest number among {num1}, {num2}, and {num3} is: {greatest}")


# WAP to check if a number is a muliple of 7 or not.

num = int(input("Enter a number: "))
if num % 7 == 0:
    print(f"{num} is a multiple of 7.")
else:    
    print(f"{num} is not a multiple of 7.")


