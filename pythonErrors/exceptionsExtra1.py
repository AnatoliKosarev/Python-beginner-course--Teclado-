# while True:
#     user_number = input("Please enter a whole number: ")
#
#     '''
#     isnumeric() checks if value is numeric, doesn't accept negative numbers and floats
#     lstrip() strips values only from left side
#     lstrip is a bit too good, and it will strip off many - characters if it finds them.
#     That's an issue for us, because while -3 is a valid number as far as int is concerned, --3 isn't.
#     '''
#     if user_number.lstrip("-").isnumeric():
#         number = int(user_number)
#         break
#     else:
#         print("You didn't enter a valid integer!")

"""
    At this point, I think it's starting to become clear that we're on the wrong path. Even for this very simple case, 
    we're having to manually deal with lots of edge cases, and it can be difficult to know if we're missing something.

    This kind of approach is called "asking for permission". We're checking if something can be done in advance, and 
    then we proceed if we determine that there aren't going to be any problems. As we've seen, this approach can be 
    very messy, and can get extremely complicated.

    This is not the approach to exception handling that we take in Python. In Python, the preferred approach is to 
    simply attempt what we think may fail, and then to recover from an exception if one occurs. This turns the problem 
    into a much simpler one: knowing what exceptions might occur. In the case above, we only need to worry about one 
    exception: ValueError.

    This alternative pattern is known as "asking for forgiveness", because we're attempting something that could go 
    wrong, and then we're doing something to make amends if something does go wrong.

    Let's take a look at a new piece of syntax that will allow us to use this asking for forgiveness pattern: the try 
    statement.
    """

while True:
    try:
        number = int(input("Please enter a whole number: "))
        break
    except ValueError:
        print("You didn't enter a valid integer!")

"""
If we return from a function inside the try statement, finally will interrupt that return to run its own code first. 
You can see an example by running this code:
"""


def finally_flex():
    try:
        return
    finally:
        print("You return when I say you can return...")


finally_flex()

"""
 This property is extremely useful for any situations where vital clean up is required after an operation. 
 An example is when working with files. What happens if we encounter some problem while processing data in a file? 
 We still want to close the file when we're done, and with finally we can make sure that this happens.
 """