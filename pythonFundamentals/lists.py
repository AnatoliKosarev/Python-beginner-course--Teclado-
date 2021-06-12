friends = [
    ["bob", 24],
    ["mike", 25],
    ["ann", 21],
    ["bob", 24]
]
print(friends)

friends.append(["kip", 22])
print(friends)

friends.remove(["bob", 24])
print(friends)

del friends[0][0]
print(friends)

friends.insert(2, ["frank", 27]) # 1st arg specifies list id for inserted value
print(friends)

friends.pop()
print(friends)

frank_info = friends.pop(2)
print(friends)
print(frank_info)

extra_friends = [
    ["phil", 23],
    ["al", 19]
]
friends.extend(extra_friends)
print(friends)

# extend() can accept any iterable, while using something like + to perform concatenation only works when both objects are lists
list1 = [1, 2, 3]
tuple1 = (4, 5, 6)
list1.extend(tuple1)
print(list1)
# print(l1 + t1) will give an error TypeError: can only concatenate list (not "tuple") to list

total = sum(list1)
length = len(list1)
average = total / length
print("Average value: " + str(average))

print(len(friends))
print(friends[1][0])

friends.clear()
print(friends)

# tuples are immutable - cannot be changed (no append(), pop() etc methods)
tuple_example = "john", "paul", "george", "ringo"
tuple_example2 = ("john", "paul", "george", "ringo")
tuple_example3 = "john",
list_example_with_tuples = [
    ("john", "paul", "george", "ringo"),
    ("james", "cliff", "kirk", "lars")
]
print(list_example_with_tuples[0][1])
print(len(tuple_example))


test_list = ["john", "paul", "george", "ringo"]
test_list.reverse()
print(test_list)
