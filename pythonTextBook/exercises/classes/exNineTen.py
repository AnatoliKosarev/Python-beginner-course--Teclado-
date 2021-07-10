from HelloWorld.pythonTextBook.exercises.classes.exNineFour import Restaurant

rest = Restaurant("Bob's", "vegan")
rest.describe_restaurant()
rest.set_number_served(100)
rest.describe_restaurant()
rest.increment_number_served(5)
rest.describe_restaurant()
rest.restaurant_open()