def city_country(city: str, country: str) -> str:
    return f"{city.title()}, {country.title()}"


print(city_country("santiago", "chile"))
print(city_country(country="EnglanD", city="london"))