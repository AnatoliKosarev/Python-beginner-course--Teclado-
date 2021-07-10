from collections import deque
from types import coroutine

friends = deque(('john', 'james', 'cliff', 'kirk', 'paul'))


@coroutine
def friend_upper():
    while friends:
        friend = friends.popleft().upper()
        greeting = yield
        print(f'{greeting} {friend}')


async def greet(g):
    print("Starting")
    await g  # finishes only after friend_upper() and its while loop is done (friends list is empty)
    print("Ending")


greeter = greet(friend_upper())
greeter.send(None)
greeter.send("hello")
greeting = input("Enter greeting: ")
greeter.send(greeting)
for _ in range(3):
    greeter.send("howdy")