favourite_places = {
    'bob': ['home', 'parent house', 'work office'],
    'kate': ['grodno', 'minsk']
}

# for person, places in favourite_places.items():
#     print(f"{person.title()}, places: ")
#     for place in places:
#         print(f"\t{place}")

for person, places in favourite_places.items():
    print(f"{person.title()}, places: {', '.join(places)}.")