rivers = {
    'nile': 'egypt',
    'neman': 'belarus',
    'mississippi': 'usa'
}

for river, country in rivers.items():
    if country == 'usa':
        formatted_country = country.upper()
    else:
        formatted_country = country.title()
    print(f'The {river.title()} runs through {formatted_country}.')

for river in rivers:
    print(river.title())

for country in rivers.values():
    if country == 'usa':
        formatted_country = country.upper()
    else:
        formatted_country = country.title()
    print(formatted_country)
