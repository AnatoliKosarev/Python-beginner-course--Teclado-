# functions can be assigned to different variables and accessed via such new variables
def greet():
    print("Hello")

hello = greet # assigning function to variable

hello() # running assigned function
greet()

#_________________________________________________________________

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

operation = operations.get(selected_option) # assigning function to variable

if operation:
    a = int(input("Please enter a value for a: "))
    b = int(input("Please enter a value for b: "))

    print(operation(a, b)) # running assigned function
else:
    print("Invalid selection")