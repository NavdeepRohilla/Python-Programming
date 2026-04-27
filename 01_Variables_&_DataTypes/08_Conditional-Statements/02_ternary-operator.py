# Single line if-else statement is called ternary operator

food = input("food : ")
eat = "Yes" if food == "Pizza" else "No"
print(eat)

food = input("food : ")
print("sweet") if food == "cake" or food == "jalebi" else print("salty")

# Clever if-else statement


age = int(input("age : "))
vote = ("yes" , "no")[age < 18]

sal = float(input("salary : "))
tax = (sal * 0.1 , sal * 0.2)[sal > 50000]
print(tax)