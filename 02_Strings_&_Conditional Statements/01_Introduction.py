# String -> A string is a sequence of characters enclosed in single quotes (' '), double quotes (" "), or triple quotes (''' ''' or """ """). Strings are used to represent text data in Python.

# Escaping Characters in Strings
# To include special characters in a string, you can use the backslash (\) to escape them. For example:
str1 = 'It\'s a nice day'
str2 = "She said, \"Hello!\""
print(str1)
print(str2)

# Escaping Newlines and Tabs
str3 = "Hello\nWorld"  # Newline
str4 = "Name\tAge\tCity"  # Tab
print(str3)
print(str4)


# Basic String Operations
# *************************Concatenation*************************
str1 = "Hello"
str2 = "World"
result = str1 + " " + str2
print("Concatenation : ", result)

# **********************************Length of String**************************
str1 = "Code with"
print("Length of str1", len(str1))
str2 = "Navdeep"
print("Length of str2", len(str2))

print("Length of string : ", len(str1 + str2))

# **************************String Indexing**************************
str4 = "Programming"
print("First character : ", str4[0])
print("Last character : ", str4[-1])

# **************************Repetition**************************
str3 = "Python "* 3
print("Repetition : ", str3)


# **************************String Slicing**************************

# +ve indexing
print("Substring (0-5) : ", str4[0:6]) # end index is not allowed
print("Substring (3-8) : ", str4[3:9])
print("Substring (5-end) : ", str4[5:])
print("Substring (5-end) : ", str4[5: len(str4)])

# -ve indexing

str = "Apple"
print("Remaining String : ", str[-3:-1])
