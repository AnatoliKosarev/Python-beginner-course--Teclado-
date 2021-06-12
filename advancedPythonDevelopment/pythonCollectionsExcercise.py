from collections import defaultdict, OrderedDict, namedtuple, deque


def task1() -> defaultdict:
    task1_object = defaultdict(lambda: "Unknown")
    task1_object["Alan"] = "Manchester"
    return task1_object


def task2(arg_od: OrderedDict) -> OrderedDict:
    if arg_od:
        arg_od.popitem()  # remove last (LIFO)
        arg_od.popitem(last=False)  # remove first (FIFO)
        if "Bob" and "Dan" in arg_od.keys():
            arg_od.move_to_end("Bob")  # move Bob to the end
            arg_od.move_to_end("Dan", last=False)  # move Dan to the start
    return arg_od


arg_od = OrderedDict([("Alan", "Manchester"),
                      ("Ddan", "Paris"),
                      ("Chris", "Lisbon"),
                      ("Eden", "Liverpool"),
                      ("Bdob", "London"),
                      ("Frank", "Newcastle")
                      ])
print(task2(arg_od))


def task3(name: str, club: str) -> namedtuple:
    Player = namedtuple("Player", ["name", "club"])
    return Player(name, club)


print(task3("Henry", "Arsenal"))


def task4(arg_deque: deque):
    if deque:
        arg_deque.pop()
        arg_deque.rotate(-1)  # same as arg_deque.append(arg_deque.popleft())
        arg_deque.appendleft("Zack")


friends = deque(('Rolf', 'Charlie', 'Jen', 'Anna'))
task4(friends)
print(friends)
