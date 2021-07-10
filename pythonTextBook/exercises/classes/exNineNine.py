from HelloWorld.pythonTextBook.exercises.classes.battery import Battery


class ElectricCar:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.battery = Battery()


if __name__ == "__main__":
    car = ElectricCar("Tesla", "S", "2021")
    car.battery.get_range()
    car.battery.upgrade_battery()
    car.battery.get_range()