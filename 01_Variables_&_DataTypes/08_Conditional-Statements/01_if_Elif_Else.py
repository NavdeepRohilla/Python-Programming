# Traffic light program

light = input("Enter the traffic light color (red, yellow, green): ")   
if light == "red":
    print("Stop")
elif light == "yellow":
    print("Ready")
elif light == "green":
    print("Go")
else:
    print("Invalid traffic light color")


# Grade of students program

marks = int(input("Enter the marks of student : ")) 
if marks >= 90:
    print("Grade A")
elif marks >= 80:
    print("Grade B")
elif marks >= 70:
    print("Grade C")
elif marks >= 60:
    print("Grade D")
else:
    print("Grade F") 