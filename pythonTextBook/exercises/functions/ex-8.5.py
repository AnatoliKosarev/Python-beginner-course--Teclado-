def describe_city(city: str, country: str = "England"):
    print(f"{city.title()} is in {country.title()}")


describe_city("London")
describe_city("Dublin", "Ireland")
describe_city("Liverpool")