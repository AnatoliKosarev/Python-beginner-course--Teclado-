def make_car(make, model, **car_info):
    car_info["make"] = make
    car_info["model"] = model
    return car_info


car = make_car("kia", "x", color="white", year="2021")
car2 = make_car("skoda", "fabia", engine="1.8", new=False)
print(car)
print(car2)
