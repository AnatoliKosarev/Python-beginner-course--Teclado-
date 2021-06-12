import itertools

numbers = [(23, 3, 56), (98, 1034, 54), (254, 344, 5), (45, 2), (122, 63, 74)]

sum_numbers = map(sum, numbers)

try:
    print(next(sum_numbers))  # 82
    print(next(sum_numbers))  # 1186
except StopIteration:
    print("Iterator is empty")

"""
 we have three employees that will take turns to lock up the shop each night. For example, if we start with employee A,
they will close up on the first day, then employee B, followed by employee C. The cycle then starts over on day 4 with
employee A.
In order to create this cycling behaviour we're going to be using a very useful function in the itertools module 
called cycle. cycle is a special type of iterator that will provide us an infinite number of results in some 
predefined sequence.
"""
employees = itertools.cycle(["Peter", "Fiona", "Carl"])
days = itertools.cycle(["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"])

for day_number in range(1, 31):
    print(f"Day {day_number} ({next(days)}): {next(employees)} closes.")
