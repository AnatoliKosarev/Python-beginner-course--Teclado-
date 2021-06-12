friends = ["Rolf", "John", "Anna"]
for counter, friend in enumerate(friends, start=1):
    print(counter, friend)
# 1 Rolf
# 2 John
# 3 Anna

friends = ["Rolf", "John", "Anna"]
friends_dict = dict(enumerate(friends))
print(friends_dict) # {0: 'Rolf', 1: 'John', 2: 'Anna'}

# если не переводить в другой тип (dict, list, etc.) - enumerate очиститься после первого цикла, т.к. использует iterator(), например:
friends = ["Rolf", "John", "Anna"]
friends_dict2 = enumerate(friends)
for counter, name in friends_dict2:
    print(counter, name)
friends_dict3 = list(friends_dict2)
print(len(friends_dict3))


movies = [
    (
        "Eternal Sunshine of the Spotless Mind",
        "Michel Gondry",
        2004
    ),
    (
        "Memento",
        "Christopher Nolan",
        2000
    ),
    (
        "Requiem for a Dream",
        "Darren Aronofsky",
        2000
    )
]
for counter, (title, director, year) in enumerate(movies, start=1): # enumerate = (2, ("Memento", "Christopher Nolan", 2000)) for each tuple
    print(f"{counter}. {title} ({year}), by {director}")                # that's why скобки (title, director, year) важны, если без них - мы хотим четыре элемента, хотя по факту у нас их 2 - counter, tuple,
                                                                        # а со скобками - мы асайним в переменные значения из tuple