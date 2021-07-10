cities = {
    'minsk': {
        'country': 'Belarus',
        'population': '5000000',
        'fact': 'Capital city'
    },
    'Moscow': {
        'country': 'Russia',
        'population': '10000000',
        'fact': 'Capital city'
    },
    'LA': {
        'country': 'USA',
        'population': '15000000',
        'fact': 'in California'
    }
}

for name, city_info in cities.items():
    print(f"{name.upper()}:") if name.lower() == "la" else print(f"{name.title()}:")
    print(f"\tCountry: {city_info['country']}")
    print(f"\tPopulation: {int(city_info['population']):,}")
    print(f"\tFact: {city_info['fact']}")

for name, city_info in cities.items():
    name = name.upper() if name.lower() == "la" else name.title()
    country, population, fact = city_info.values()
    print(f"{name} in country {country} with the population {int(population):,}, fun fact: {fact}.")