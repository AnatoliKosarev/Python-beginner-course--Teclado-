"""
LookupError is use any time a key or index is not found, and it has two "children": IndexError and KeyError. The latter
two are going to be a lot more familiar to us than LookupError, because those are the exceptions actually raised by
things like lists, dictionaries, and tuples.

However, both IndexError and KeyError are considered to also be a LookupError, so it's perfectly legal for us to handle
these exceptions like this:
"""

numbers = [1, 2, 3, 4, 5]

try:
    print(numbers[100])  # <- Out of range index
except LookupError:
    print("Could not retrieve that value.")
"""
Here what actually gets raised is an IndexError, but our except clause catches the exception nonetheless.

It's easy to see how this kind of pattern could be useful in cases where we have some flexible piece of code that can 
work with both sequences and mapping types like dictionaries.

It also gives us the ability to catch general exceptions as a fallback for more specific exceptions.
"""
numbers = [1, 2, 3, 4, 5]

try:
    print(numbers[100])  # <- Out of range index
except IndexError:
    print("The requested index is out of range")
except LookupError:
    print("Could not retrieve that value.")

person = {
    "name": "Phil",
    "city": "Budapest"
}

try:
    print(person["age"])  # <- Referencing an undefined key
except IndexError:
    print("The requested index is out of range")
except LookupError:
    print("Could not retrieve that value.")

"""
Sometimes it can be useful to get hold of the original exception message, for example if we want to use it for 
logging purposes.

In these situations we can use the as keyword as part of an except clause, putting a variable name directly after the 
as keyword. This variable name gives us a handle that we can use to access information pertaining to the original 
exception.
"""
numbers = [1, 2, 3, 4, 5]

try:
    print(numbers[100])  # <- Out of range index
except LookupError as ex:
    print(f"Error: {ex}")

"""
Re-raising an exception
We can also use raise in another way inside an except clause. By writing raise without specifying an exception, we can 
re-raise the exception we caught in our except clause.

This is very useful in cases where we don't actually want to stop an exception from happening, we just want to do 
something with the exception before the exception terminates the application.

Once again, logging is a good example here. We may want to use information from the original exception for our logs so 
that we have a permanent record of what went wrong, and then we can allow the exception to terminate the program.
"""

"""
Nested try statements
One thing you may not have realised is that we can put try statements inside other try statements. This can be very useful if we want to try to recover from some other exception, but we're not really sure if our fix is going to work.

Let's say that I'm going to be reading a very large number of numbers from a file, and I want to convert the string representation of each of these numbers to an integer. I'm fairly certain that nearly all of the numbers are going to be integers, but every now and again, I may run across a string representation of a float instead.

For simplicity's sake, lets assume that all of the numbers are on different lines in the file, so we can just iterate over the file to get what we need.

Because there's a chance I may run across a float in the file, I can't just do something like this:

with open("numbers.txt", "r") as numbers_file:
	numbers = [int(number) for number in numbers_file]
If we try to pass a string representation of a float to the int function, for example "93.2", the program is going to terminate, because a ValueError will be raised by int.

To get around this, I'm going to define a function that is going to do the conversion for us. Inside this function I'm first going to try to convert the number to an integer using int, and if this fails, I'm going to try to convert it to a float instead.

Should the integer conversion go well, I'm just going to return the new integer. If we get a float, I'm going to round that float using the round function, and then I'm going to return the resulting integer.

Should all of this fail, then there's nothing more we can do, so I'm going to raise a ValueError with my own custom message.
"""


def intify(number):
    try:
        return int(number)
    except ValueError:
        try:
            f_number = float(number)
        except ValueError:
            raise ValueError(f"could not convert string to an integer: {number}")
        else:
            return round(f_number)


# with open("numbers.txt", "r") as numbers_file:
# numbers = [intify(number) for number in [1, 2, "12qw"]]
"""
Controlling the traceback
One problem with the approach above is that my traceback is really big, and not very helpful:

Traceback (most recent call last):
  File "pee.py", line 3, in intify
    return int(number)
ValueError: invalid literal for int() with base 10: '"f"'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "pee.py", line 6, in intify
    f_number = float(number)
ValueError: could not convert string to float: '"f"'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "pee.py", line 14, in <module>
    numbers = [intify(number) for number in numbers_file]
  File "pee.py", line 14, in <listcomp>
    numbers = [intify(number) for number in numbers_file]
  File "pee.py", line 8, in intify
    raise ValueError(f"could not convert string to an integer: {number}")
ValueError: could not convert string to an integer: "f"
There's a lot of information here that I don't really need the user to see, because it mostly describes implementation 
details. I've also defined by own custom error message which explains everything the user needs to know about the 
situation.

To get rid of all of this extra traceback information, we can use another keyword in conjunction with raise called from.

from will let us specify a point from which we want to start the traceback information. We can do this by referring to 
an exception by name (remember that we can name exceptions using as). Alternatively we can write None in place of an 
exception name.

None is going to get rid of all of this excess traceback information from this try statement, and just leave us with the 
most recent exception.
"""


def intify(number):
    try:
        return int(number)
    except ValueError:
        try:
            f_number = float(number)
        except ValueError:
            raise ValueError(f"could not convert string to an integer: {number}") from None
        else:
            return round(f_number)


#with open("numbers.txt", "r") as numbers_file:
numbers = [intify(number) for number in [1, 2, "12qw"]]

"""
Now our traceback is much more readable.

Traceback (most recent call last):
  File "pee.py", line 14, in <module>
    numbers = [intify(number) for number in numbers_file]
  File "pee.py", line 14, in <listcomp>
    numbers = [intify(number) for number in numbers_file]
  File "pee.py", line 8, in intify
    raise ValueError(f'could not convert string to an integer: {number}') from None
ValueError: could not convert string to an integer: "12qw"
"""
