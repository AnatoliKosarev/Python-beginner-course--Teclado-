
def divide_normal(a, b):
    return a /b

"""
lambda has to be assigned to a var, otherwise will be destroyed after creation
"""
divide_lambda = lambda x, y: x / y # lambda <arguments>: <return value>

print(divide_lambda(15, 3))

"""
____________________________________________________________
Functions as arguments
"""
def get_grade_average(student):
    return student["grade_average"]

students = [
    {"name": "Hannah", "grade_average": 83},
    {"name": "Charlie", "grade_average": 91},
    {"name": "Peter", "grade_average": 85},
    {"name": "Rachel", "grade_average": 79},
    {"name": "Lauren", "grade_average": 92}
]

valedictorian = max(students, key=get_grade_average)
print(valedictorian)
"""
Here we provided the get_grade_average function as an argument for max, and max called this function for us internally 
to determine the order of the items in our list. It then correctly returned this dictionary as the student with 
the highest grade average.

There are other functions and methods which expect similar sort of functions. For example, the sorted function 
and sort methods both accepts keys, which must be functions.
____________________________________________________________
Returning functions from other functions
"""
def add(a, b):
    print(a + b)

def subtract(a, b):
    print(a - b)

def multiply(a, b):
    print(a * b)

def divide(a, b):
    if b == 0:
        print("You can't divide by 0!")
    else:
        print(a / b)

operations = {
    "a": add,
    "s": subtract,
    "m": multiply,
    "d": divide
}
# It's really important to note that we're not calling the functions here: we're just referencing the functions
# using their variable names.
# Now we have a dictionary where the keys are strings and the values associated with those keys are functions.
# We can now ask the user to select from these options, and we'll run the function for them by looking up their option
# in the dictionary:

selected_option = input("""Please select one of the following options:

a: add
s: subtract
m: multiply
d: divide

What would you like to do? """)

operation = operations.get(selected_option)

if operation:
    a = int(input("Please enter a value for a: "))
    b = int(input("Please enter a value for b: "))

    operation(a, b)
else:
    print("Invalid selection")
# When we call get, we look up the user's string in our dictionary, and (assuming nothing went wrong) what we get back
# is a function. We can then assign this function to a variable name and call it just like any other function.
# If something did go wrong, we have some protection, because the get method returns None when the key isn't found,
# and we can check for this using a conditional statement to make sure we didn't get a falsy value. If we did, we know
# that we didn't get a function back, so we can let the user know their selection was invalid.
"""
____________________________________________________________
Lambda expressions
with the above "valedictorian" example with lambda
"""
students = [
    {"name": "Hannah", "grade_average": 83},
    {"name": "Charlie", "grade_average": 91},
    {"name": "Peter", "grade_average": 85},
    {"name": "Rachel", "grade_average": 79},
    {"name": "Lauren", "grade_average": 92}
]

valedictorian = max(students, key=lambda student: student["grade_average"])
print(valedictorian)


# with the above "operations" example
def divide(a, b):
    if b == 0:
        return "You can't divide by 0!"
    else:
        return a / b

operations = {
    "a": lambda a, b: a + b,
    "s": lambda a, b: a - b,
    "m": lambda a, b: a * b,
    "d": divide
}

selected_option = input("""Please select one of the following options:

a: add
s: subtract
m: multiply
d: divide

What would you like to do? """)

operation = operations.get(selected_option)

if operation:
    a = int(input("Please enter a value for a: "))
    b = int(input("Please enter a value for b: "))

    print(operation(a, b))
else:
    print("Invalid selection")
# The only function we can't replace here is divide, because divide has a conditional statement inside.
# Lambda expressions are limited to single expressions and cannot contain statements.
