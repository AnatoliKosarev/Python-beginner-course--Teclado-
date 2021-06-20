def get_formatted_city_country(country: str, city: str, population="") -> str:
    if population:
        formatted_result = f"{city.title()}, {country.title()} - population {population}"
    else:
        formatted_result = f"{city.title()}, {country.title()}"
    return formatted_result

