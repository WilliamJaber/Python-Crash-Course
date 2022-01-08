def city_country(city, country):
    """Return's a string formatted of the city and country"""
    return f'{city.title()}, {country.title()}. '

city_location_1 = city_country('medellin', 'colombia')
print(city_location_1)

city_location_2 = city_country('caracas', 'venezuela')
print(city_location_2)

city_location_3 = city_country('new york', 'united states')
print(city_location_3)
