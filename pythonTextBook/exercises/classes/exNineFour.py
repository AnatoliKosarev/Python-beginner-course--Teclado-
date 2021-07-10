class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def __repr__(self):
        return f"Name: {self.restaurant_name}, type: {self.cuisine_type}"

    def set_number_served(self, number):
        self.number_served = number

    def increment_number_served(self, number):
        self.number_served += number

    def describe_restaurant(self):
        print(f"{self.restaurant_name}, {self.cuisine_type}, {self.number_served}")

    def restaurant_open(self):
        print(f"Restaurant {self.restaurant_name} is open")


if __name__ == "__main__":
    rest = Restaurant("McD", "fast-food")
    print(rest.number_served)
    rest.number_served = 1
    print(rest.number_served)
    rest.set_number_served(2)
    print(rest.number_served)
    rest.increment_number_served(10)
    print(rest.number_served)
    print(rest)
    print(__name__)