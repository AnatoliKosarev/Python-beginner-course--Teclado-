message = "My friends are {friends}"
list1 = ["john", "paul", "george", "ringo"]
print(message.format(friends=list1))
comma_separated = ", ".join(list1)
print(message.format(friends=comma_separated))
print(message.format(friends=", ".join(list1)))

numbers = [1, 2, 3, 4]
str_numbers = []
for number in numbers:
    str_numbers.append(str(number))
print(", ".join(str_numbers))


user_input = input("Please enter 5 digits separated with a coma: ")
user_input_list = user_input.split(",")
print(user_input_list)
user_input_tuple = tuple(user_input.split(","))
print(user_input_tuple)
user_input_set = set(user_input.split(","))
print(user_input_set)
# If we don’t specify a separator sequence for split, it’s going to split based on any length of whitespace.

# to get rid of spaces
number_list_without_spaces = []
for number in str_numbers:
    number_list_without_spaces.append(number.strip())
print(str_numbers)

# We don’t always need to call split. If we just want to put every character as a different item in a list or tuple,
# we can just pass the string to the list or tuple function instead:
sample_string = "Python"
print(list(sample_string))  # ['P', 'y', 't', 'h', 'o', 'n']
print(tuple(sample_string))  # ('P', 'y', 't', 'h', 'o', 'n')