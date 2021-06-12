currencies = (0.8, 1.2)
usd, eur = currencies
print(usd)
print(eur)

friends = [("john", 25), ("paul", 26), ("george", 23), ("ringo", 27)]
for name, age in friends:
    print(f"{name} is {age} years old.")

head, *tail = [1, 2, 3, 4, 5]
print(head)  # 1
print(tail)  # [2, 3, 4, 5]

*head, tail = [1, 2, 3, 4, 5]
print(head)  # [1, 2, 3, 4]
print(tail)  # 5

head, *middle, tail = [1, 2, 3, 4, 5]
print(head)    # 1
print(middle)  # [2, 3, 4]
print(tail)    # 5

# ignoring value
person = ("Bob", 42, "Mechanic")
name, _, profession = person
print(name, profession)  # Bob Mechanic