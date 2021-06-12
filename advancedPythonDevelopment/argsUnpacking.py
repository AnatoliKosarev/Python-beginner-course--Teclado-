def sum_custom(*args):
    print(sum(args))


sum_custom(1, 2, 3)


def print_args(*args, **kwargs):
    for arg in args:
        print(f"{arg} is pos. arg")

    for kwarg in kwargs.values():
        print(f"{kwarg} is a key arg")


print_args(1, "qwe", 45, mile=222, joe="ferw")


def print_dict(country):
    print("name is {name}, population is {population}, capital is {capital}, currency is {currency}".format(**country))


country = {
    "name": "Germany",
    "population": "83 million",
    "capital": "Berlin",
    "currency": "Euro"
}

print_dict(country)


print(*range(1, 20), sep=",")


class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

users = [
    { 'username': 'rolf', 'password': '123' },
    { 'password': 'youaretoo', 'username': 'tecladoisawesome'}
]

user_objects = [User(**data) for data in users]
print(user_objects[0].username, user_objects[0].password, user_objects[1].username, user_objects[1].password)
