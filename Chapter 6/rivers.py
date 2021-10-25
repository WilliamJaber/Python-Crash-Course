rivers = {
    'amazon': 'Brazil, Bolivia, Perú, Ecuador, Colombia, Venezuela, French Guian and Suriname',
    'nilo': 'Egypt',
    'Yangtze': 'China',
    }

# Use a loop to print a sentence about each river.
for name, country in rivers.items():
    print(f'{name.title()}, runs through {country}.\n')

# Use a loop to print the name of each river included in the dictionary.
for name in rivers.keys():
    print(f"River's name: {name.title()}")

# Use a loop to print the name of each country included in the dictionary.
for country in rivers.values():
    print(f"Country: {country.title()}")
