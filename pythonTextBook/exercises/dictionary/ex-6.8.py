pets = [
    {'type': 'dog', 'owner': 'William'},
    {'type': 'cat', 'owner': 'Anna'},
    {'type': 'hamster', 'owner': 'Luke'}
]

# for pet in pets:
#     for pet_data in pet.values():
#         print(pet_data)


for pet in pets:
    type, owner = pet.values()
    print(f"{type}, owner {owner}")

