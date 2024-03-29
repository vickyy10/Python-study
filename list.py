my_list = [1, 2, 3, 4, 5]

# Change an element
my_list[2] = 10
print(my_list)  # Output: [1, 2, 10, 4, 5]

# Add an element to the end of the list
my_list.append(6)
print(my_list)  # Output: [1, 2, 10, 4, 5, 6]

# Remove an element by value
my_list.remove(4)
print(my_list)  # Output: [1, 2, 10, 5, 6]

# Insert an element at a specific index
my_list.insert(2, 3)
print(my_list)  # Output: [1, 2, 3, 10, 5, 6]

# Delete an element by index
del my_list[3]
print(my_list)  # Output: [1, 2, 3, 5, 6]
