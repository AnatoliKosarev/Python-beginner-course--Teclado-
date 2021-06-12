# reverse() function - we can't use it on other sequence types, like tuples and strings,
# and it also performs an in-place modification of the original sequence
friends_list = ["Rolf", "John", "Mary"]
friends_reversed = friends_list[::-1]
print(friends_list)
print(friends_reversed)  # ['Mary', 'John', 'Rolf']

friends_tuple = ("Rolf", "John", "Mary")
friends_tuple_reversed = friends_tuple[::-1]
print(friends_tuple)
print(friends_tuple_reversed)  # ['Mary', 'John', 'Rolf']

greet = "Hello, World!"
greet_reversed = greet[::-1]
print(greet)
print(greet_reversed)  # "!dlroW ,olleH"