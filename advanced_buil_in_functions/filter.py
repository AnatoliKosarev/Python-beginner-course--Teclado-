friends = ["Rolf", "Anna", "Randy", "Bob"]


def starts_with_r(friend):
    return friend.startswith("R")


names_starts_with_r = filter(starts_with_r, friends)

# names_starts_with_r = filter(lambda friend: friend.startswith("R"), friends)

# names_starts_with_r = (friend for friend in friends if friend.startswith("R"))

"""
same as filter() or conditional comprehension 
"""


def my_custom_filter(func, iterable):
    for i in iterable:
        if func(i):
            yield i


print(names_starts_with_r)
print(next(names_starts_with_r))

for friend in names_starts_with_r:
    print(friend)

"""
filter() returns generator

Instead of passing in a function to filter, it's possible to use the value None. This tells filter that we want to use 
the truth values of the values directly, instead of performing some kind of comparison, or calculating something.

In this case, filter will keep all truthy values from the original iterable, and all falsy values will be discarded.
"""

values = [0, "Hello", [], {}, 435, -4.2, ""]
truthy_values = filter(None, values)

print(*truthy_values, sep=", ")  # Hello, 435, -4.2
