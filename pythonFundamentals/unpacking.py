movie = ("12 Angry Men", "Sidney Lumet", 1957)
title, director, year = movie


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
for title, director, year in movies:
    print(f"{title} ({year}), by {director}")