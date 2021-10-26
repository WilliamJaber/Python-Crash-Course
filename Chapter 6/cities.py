cities = {
    'medellin': {
        'country': 'colombia',
        'population': '2.5 M',
        'fact': 'is known as the "City of the Eternal Spring."',
        },
    'miami': {
        'country': 'united states',
        'population': '442 K',
        'fact': 'it is the only US city that was founded by a woman.',
        },
    'new york': {
        'country': 'united states',
        'population': '8.4 M',
        'fact': "The City's Original Name Was New Amsterdam.",
        },
    }

for city, info in cities.items():
    print(f"\nCity's name: {city.upper()}")
    for descr, value in info.items():
        print(f'\t{descr.title()}: {value}')
