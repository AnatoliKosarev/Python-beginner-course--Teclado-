friend_age = {}
friend_age = {"Bob": 24, "Ann": 22, "Kate": 25}
print(friend_age)

print(friend_age["Kate"])

friend_age["Max"] = 35
print(friend_age)

friend_age["Ann"] = 23
print(friend_age)

friends2 = [("Bob", 24), ("Ann", 22), ("Kate", 25)]
friends_dict = dict(friends2)
print(friends_dict)

friends = (
    {"name": "Bob Smith", "age": 24},
    {"name": "Mike Johns", "age": 20},
    {"name": "Ann Rice", "age": 21}
)

friends[0]["grades"] = [5, 6, 9]
print(friends)

student_data = {
    "class": "OM1",
    "sex": "male"
}

friends[0].update(student_data)
print(friends)

del friends[0]["sex"]
print(friends)

bob_smith_class = friends[0].pop("class")
print(bob_smith_class)
print(friends)
print()

for key in friends[0]:
    print(key)
print()

for value in friends[0].values():
    print(value)
print()

for key1, value1 in friends[0].items():
    print(f"{key1}: {value1}")
print()

# throws KeyError: 'names' if key doesn't exist
print(friends[0]["name"])
# returns None if key doesn't exist without crashing
print(friends[0].get("names"))
# or specified value
print(friends[0].get("names", 0))

friends[0].clear()
print(friends)
