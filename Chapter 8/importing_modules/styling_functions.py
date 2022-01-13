# make sure they follow the styling guidelines described in this section
def make_album(
    artist_name, album_title,
    num_of_songs = None):
    """Builds a dictionary describing a music album"""

    album = {'Artist': artist_name.title(), 'Album': album_title.title()}
    if num_of_songs:
        album['num_of_songs'] = num_of_songs
    return album


def make_car(manufacturer, model, **extras) -> dict:
    """Builds a dictionary containing information about a car"""

    extras['manufacturer'] = manufacturer
    extras['model'] = model
    return f'\n{extras}\n'

car_info = make_car(
    'BMW', 'X5', color = 'white',
    seats_color = 'Red', luxury_wheels = True)

print(car_info)


def build_profile(first, last, **user_info) -> dict:
    """Build a dictionary containing everything we know about a user."""

    user_info['first_name'] = first
    user_info['last_name'] = last
    return f'\n{user_info}\n'

user_profile = build_profile(
    'William', 'Jaber', age = 27,
    location = 'South America', field = 'Programming')

print(user_profile)
