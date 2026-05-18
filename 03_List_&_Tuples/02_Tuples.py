'''
Tuples in python --> A built in data type that lets us create immutable sequences of values.

- Tuples are immutable, meaning once they are created, their content cannot be changed.

- Tuples are ordered, meaning the elements have a specific order and can be accessed using their index (starting from 0).

- Tuples can contain duplicate elements.

'''

tup = (1, 2, 3, 4, 5)
print(tup)
print(type(tup))

tup[0] = 10  # This will raise a TypeError because tuples are immutable


print(tup[0])  # Output: 1
print(tup[1:4])  # Output: (2, 3, 4)

# Empty tuple
empty_tuple = ()
print(empty_tuple)  # Output: ()

# Tuple with one element (note the comma)
single_element_tuple = (42,)
print(single_element_tuple)  # Output: (42,)

# Tuple unpacking
a, b, c, d, e = tup
print(a)  # Output: 1
print(b)  # Output: 2
print(c)  # Output: 3
print(d)  # Output: 4
print(e)  # Output: 5

# Slicing a tuple
print(tup[1:4])  # Output: (2, 3, 4)

# Tuple Methods

# 1. count() - Returns the number of occurrences of a specified value
print(tup.count(2))  # Output: 1

# 2. index() - Returns the index of the first occurrence of a specified value
print(tup.index(3))  # Output: 2