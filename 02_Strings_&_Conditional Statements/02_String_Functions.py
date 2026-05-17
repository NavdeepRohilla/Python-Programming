# String Functions in Python
# Python provides several built-in functions that can be used to manipulate strings. Here are some commonly used string functions:

# 1. len() - Returns the length of a string

# 2. lower() - Converts a string to lowercase

# 3. upper() - Converts a string to uppercase

# 4. strip() - Removes leading and trailing whitespace from a string
# 5. replace() - Replaces a specified substring with another substring
# 6. split() - Splits a string into a list of substrings based on a specified delimiter

# 7. join() - Joins a list of strings into a single string with a specified delimiter

# 8. find() - Returns the index of the first occurrence of a specified substring in a string

# 9. count() - Returns the number of occurrences of a specified substring in a string

# 10. isalpha() - Returns True if all characters in the string are alphabetic, otherwise returns False

# 11. isdigit() - Returns True if all characters in the string are digits, otherwise returns False

# 12. isalnum() - Returns True if all characters in the string are alphanumeric, otherwise returns False

# 13. startswith() - Returns True if the string starts with a specified substring, otherwise returns False

# 14. endswith() - Returns True if the string ends with a specified substring, otherwise returns False


str = "I am a coder"
print(len(str))
print(str.lower()) # Converts the string to lowercase

print(str.upper()) # Converts the string to uppercase

print(str.strip()) # Removes the leading and trailing whitespace from the string

print(str.replace("coder", "developer")) # Replaces the specified substring with another substring

print(str.split(" "))

print(str.join("a b c")) # Joins the list of strings into a single string with a specified delimiter

print(str.find("coder"))

print(str.count("a")) # Returns the number of occurrences of a specified substring in a string

print(str.startswith("I am"))

print(str.endswith("coder")) # Returns True if the string ends with a specified substring, otherwise returns False


