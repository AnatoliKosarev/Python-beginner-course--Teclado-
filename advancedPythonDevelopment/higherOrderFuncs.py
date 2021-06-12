"""
Higher order functions are functions that receive other functions as arguments
"""

movies = [
    {"name": "The Matrix", "director": "Wachowski"},
    {"name": "Klaus", "director": "Pablos"},
    {"name": "Irishman", "director": "Scorsese"},
    {"name": "Iron man", "director": "Johnes"}
]

"""
Pass in function <finder> and call it inside
"""
def find_movie(expected_value: str, finder) -> list:
    find_list = []
    for movie in movies:
        if expected_value.lower() in finder(movie).lower():
            find_list.append(movie)
    return find_list


find_by = input("What property are you searching by? ")
looking_for = input("What are you looking for? ")
results = find_movie(looking_for, lambda movie: movie[find_by])
print(results or "No movies found")
