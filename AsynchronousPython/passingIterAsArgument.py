from collections import deque

friends = deque(('john', 'james', 'cliff', 'kirk', 'paul'))


def friend_getter():
    yield from friends


def greet_friends(iterator):
    try:
        while True:
            friend = next(iterator)
            yield f'Hi, {friend.title()}!'
    except StopIteration:
        pass


g = greet_friends(friend_getter())
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))

