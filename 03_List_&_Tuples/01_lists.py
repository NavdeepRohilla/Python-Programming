'''
Lists in Python -> A built in data type that stors set of values. It can store elements of different types (integer, float, string, etc)

- Lists are mutable, meaning you can change their content after they are created.

- Lists are ordered, meaning the elements have a specific order and can be accessed using their index (starting from 0).

- Lists can contain duplicate elements.
'''

marks = [90, 85, 92, 88, 95]
print(marks) 
print(type(marks))

student = ["Alice", 20, "Computer Science", 3.8]
print(student)


# Accessing elements in a list
print(marks[0])  # Output: 90
print(student[0])  # Output: Alice


# Modifying elements in a list
marks[1] = 87
print(marks)  # Output: [90, 87, 92, 88, 95]

student[0] = "Navdeep"
print(student)  # Output: ['Alice', 21, 'Computer Science', 3

# Length of a list
print(len(marks))  # Output: 5
print(len(student))  # Output: 4

# List slicing
print(marks[1:4])  # Output: [87, 92, 88]
print(student[1:3])  # Output: [21, 'Computer Science']

# List Methods
# 1. append() - Adds an element to the end of the list
marks.append(93)
print(marks)  # Output: [90, 87, 92, 88, 95, 93]

# 2. insert() - Inserts an element at a specific index
student.insert(1, "Smith")
print(student)  # Output: ['Alice', 'Smith', 21, 'Computer Science

# 3. remove() - Removes the first occurrence of a specified value
marks.remove(88)
print(marks)  # Output: [90, 87, 92, 95, 93]

# 4. pop() - Removes and returns the element at a specified index (default is the last element)
last_mark = marks.pop()
print(last_mark)  # Output: 93
print(marks)  # Output: [90, 87, 92, 95]

# 5. sort() - Sorts the list in ascending order
marks.sort()
print(marks)  # Output: [87, 90, 92, 95]

list.sort(reverse=True)  # Sort in descending order
print(marks)  # Output: [95, 92, 90, 87]


# 6. reverse() - Reverses the order of the list
marks.reverse()
print(marks)  # Output: [95, 92, 90, 87]

# 7. index() - Returns the index of the first occurrence of a specified value
index_of_90 = marks.index(90)
print(index_of_90)  # Output: 2

# 8. count() - Returns the number of occurrences of a specified value
count_of_87 = marks.count(87)
print(count_of_87)  # Output: 1

# 9. clear() - Removes all elements from the list
marks.clear()
print(marks)  # Output: []

