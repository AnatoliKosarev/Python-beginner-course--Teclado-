person1 = {
    'name': 'John',
    'lastname': 'Lennon',
    'age': '33',
    'city': 'Liverpool'
}

person2 = {
    'name': 'James',
    'lastname': 'Hetfield',
    'age': '45',
    'city': 'San Francisco'
}

person3 = {
    'name': 'Fat',
    'lastname': 'Mike',
    'age': '19',
    'city': 'Los Angeles'
}

people = [person1, person2, person3]

# for person in people:
#     for data in person.values():
#         print(data)

for person in people:
    name, lastname, age, city = person.values()
    print(f"{name} {lastname}, {age}, {city}")