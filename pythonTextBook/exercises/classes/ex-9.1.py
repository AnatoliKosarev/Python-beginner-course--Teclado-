class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def __repr__(self):
        return f"Name: {self.restaurant_name}, type: {self.cuisine_type}"

    def describe_restaurant(self):
        print(f"{self.restaurant_name}, {self.cuisine_type}")

    def restaurant_open(self):
        print(f"Restaurant {self.restaurant_name} is open")


restaurant = Restaurant("McDonald's", "fast food")
print(restaurant)
print(f"{restaurant.restaurant_name} {restaurant.cuisine_type}")
restaurant.describe_restaurant()
restaurant.restaurant_open()
