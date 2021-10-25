favorite_places = {
    'gen': ['london', 'caracas'],
    'peter': ['barcelona'],
    'will': ['madrid', 'Medellin', 'new york'],
    }

# print each person’s name and their favorite places.
for name, places in favorite_places.items():
    if len(places) == 1:
        print(f"\n{name.title()}'s favorite places is:")
    else:
        print(f"\n{name.title()}'s favorite places are:")
    for place in places:
        print(f"\t{place.title()}")
