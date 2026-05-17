age = int(input("Enter Age: "))

if(age < 18): 
    print("The Person is a child.")
elif(age >= 18 and age < 60):
    print("The Person is an adult.")
else:
    print("The person is a senior citizen")

print("*********************************************************")


light = input("Enter Color: ")

if(light == "red"):
    print("Stop")
elif(light == "green"):
    print("Go")
elif(light == "yellow"):
    print("look")
else:
    print("Choose among red, yellow, green")

print("End of Loop")


marks = int(input("Enter Marks: "))
if(marks >= 90):
    grade = "A"
elif(marks >= 80 and marks < 90):
    grade = "B"
elif(marks >= 70 and marks < 80):
    grade = "C"
else:
    grade = "D"

print("Grade of the student -> " , grade)


#  Nested if-else statements

age = 34

if(age > 18):
    if(age < 60):
        print("The person is an adult.")
    else:
        print("The person is a senior citizen.")
else:
    print("The person is a child.")