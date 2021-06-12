"""
Python has a built in function called iter which returns an iterator for the iterable we provide as an argument.
"""
numbers = [1, 2, 3, 4, 5]
numbers_iter = iter(numbers)

print(numbers_iter)  # <list_iterator object at 0x7f57d138af70>

print(next(numbers_iter))  # 1
print(next(numbers_iter))  # 2

while True:
    try:
        number = next(numbers_iter)
    except StopIteration:
        break
    else:
        print(number)


def first_hundred():
    for number in range(1, 101):
        yield number


def first_hundred():
    print("First value requested\n")

    for number in range(1, 101):
        print("Starting new iteration")
        yield number
        print("Ending this iteration\n")


g = first_hundred()

print(next(g))
print(next(g))

"""
First value requested

Starting new iteration
1
Ending this iteration

Starting new iteration
2

For this second iteration, you'll note that we don't print the "Ending this iteration\n" string, because yield paused 
the execution before we reached that point.

If we were to call next again, we'd get this string printed first, before starting a third iteration of the loop.
"""

"""
When we call a generator, it gives us back a new generator iterator. Each of these generator iterators is an independent
iterator, so be careful you don't do something like this:
"""


def first_hundred():
    for number in range(1, 101):
        yield number


print(next(first_hundred()))  # 1
print(next(first_hundred()))  # 1
print(next(first_hundred()))  # 1

squares = (number ** 2 for number in range(1, 11))

for square in squares:
    print(square)

squares = (number ** 2 for number in range(1, 11))

print(*squares, sep=", ")

squares = (number ** 2 for number in range(1, 11))

print(next(squares))  # 1
print(next(squares))  # 4
print(next(squares))  # 9

names = [" rick", " MORTY  ", "beth ", "Summer", "jerRy    "]

names = (name.strip().title() for name in names)
print(next(names))


def fibonacci_numbers_generator(nums):
    x, y = 0, 1
    for _ in range(nums):
        yield x
        x, y = y, x + y



print(*fibonacci_numbers_generator(5), sep=", ")
