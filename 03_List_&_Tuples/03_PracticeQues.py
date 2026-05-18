# Wap to ask the user to enter names of thier 3 favorite movies and store them in a list.

movies = []
movie1 = input("Enter the name of your first favorite movie: ")
movie2 = input("Enter the name of your second favorite movie: ")
movie3 = input("Enter the name of your third favorite movie: ")

movies.append(movie1)
movies.append(movie2)
movies.append(movie3)

print("Your favorite movies are:" , movies)


# Wap to check if a list contains a palindrome of elements.(Hint use copy() method)

list = [1, 2, 3, 2, 1]

reversed_list = list.copy()
reversed_list.reverse()

if list == reversed_list:
    print("The list is a palindrome.")
else:
    print("The list is not a palindrome.")