from HelloWorld.pythonTextBook.exercises.classes.exNineFour import Restaurant


class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavours = ["vanilla", "chocolate", "strawberry"]

    def show_flavours(self):
        print(", ".join(self.flavours))


if __name__ == "__main__":
    print(__name__)
    ice = IceCreamStand("Bob's", "ice cream")
    ice.show_flavours()
    ice.describe_restaurant()
