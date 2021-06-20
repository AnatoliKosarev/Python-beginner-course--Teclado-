from collections import deque

friends = deque(('john', 'james', 'cliff', 'kirk', 'paul'))


def friend_upper():
    while friends:
        friend = friends.popleft().upper()
        greeting = yield
        print(f'{greeting} {friend}')


def greet(g):
    # yield from g  # same as all code after it, but as it's not intuitively clear - not supposed to be used
    g.send(None)
    while True:
        greeting = yield
        g.send(greeting)


greeter = greet(friend_upper())
greeter.send(None)  # priming greet(g), in greet(g) code stops at greeting = yield, where currently greeting = None
# greet(g) at the same time priming friend_upper() at line 15
# when priming only None can be send, otherwise - TypeError: can't send non-None value to a just-started generator
greeter.send("Hello")  # greeting = None becomes greeting = Hello and sends this value to friend_upper(), friend_upper()
# receives value on line 9 and prints it out
greeter.send(None)
# greeter.send("hi ")
# greeter.send("hi ")
# greeter.send("hi ")
for x in range(3):
    greeter.send(f"hi{x}")

