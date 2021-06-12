"""
Much like range, zip is lazy, which means it only calculates the next value when we request it.
We therefore can't print it directly, but we can convert it to something like a list if we want to see the output
"""
from itertools import zip_longest

student_ids = (112343, 134555, 113826, 124888)
names = ("mary", "Richard", "Noah", "KATE")
print(*zip(student_ids, names))
student_dict = dict(zip(student_ids, names))
print(student_dict)

student_dict2 = dict(zip(names, student_ids))
print(student_dict2)

student_dict3 = list(zip(student_ids, names, [1, 2, 3, 4, 5])) # value "5" is ignored because student_ids, names have only 4 elements, to avoid this - zip_longest should be used
print(student_dict3)


pet_owners = ["Paul", "Andrea", "Marta"]
pets = ["Fluffy", "Bubbles", "Captain Catsworth"]
for owner, pet in zip(pet_owners, pets):
    print(f"{owner} owns {pet}.")


movie_titles = [
    "Forrest Gump",
    "Howl's Moving Castle",
    "No Country for Old Men"
]
movie_directors = [
    "Robert Zemeckis",
    "Hayao Miyazaki",
    "Joel and Ethan Coen"
]
movies = list(zip(movie_titles, movie_directors)) # clears after the first loop if not converted to list, dict or tuple - list(zip(movie_titles, movie_directors))
for title, director in movies:
    print(f"{title} by {director}.")
movies_list = list(movies)
print(f"There are {len(movies_list)} movies in the collection.")
print(f"These are our movies: {movies_list}.")


"""
unzip = *zipped_collection

Using the * operator, we can break up a zip object, or really any collection of collections. 
For example, we might have something like this:
"""
zipped = [("John", 26), ("Anne", 31), ("Peter", 29)]
# We can use the * operator in conjunction with zip to split this back into names and ages:
names, ages = zip(*zipped)
print(names)  # ("John", "Anne", "Peter")
print(ages)   # (26, 31, 29)


"""
_____________________________________________________
zip_longest

when we use zip, zip will stop combining our iterables as soon as one of them runs out of elements. 
If the other iterables are longer, we just throw those excess items away. 
"""
l_1 = [1, 2, 3]
l_2 = [1, 2]
combinated = list(zip(l_1, l_2))
print(combinated)  # [(1, 1), (2, 2)]

combinated2 = list(zip_longest(l_1, l_2, fillvalue="_"))
print(combinated2)  # [(1, 1), (2, 2), (3, '_')]