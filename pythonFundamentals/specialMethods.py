class Garage:
    def __init__(self):
        self.cars = []

    def __len__(self):
        return len(self.cars)

    def __getitem__(self, item):
        return self.cars[item]

    def __repr__(self): # used for debugger if __str__() is implemented, if not - used to print object info, e.g. print(ford)
        return f"<Garage {self.cars}>"

    def __str__(self): # used for object representation for user
        return f"Garage with {len(self)} cars" # calls __len__(self) method

ford = Garage()
ford.cars.append("Fiesta")
ford.cars.append("Focus")

print(len(ford))
print(ford[0])

"""
after __getitem__ was added to Garage class - we can iterate over Garage objects
"""
for car in ford:
    print(car)

print(ford)