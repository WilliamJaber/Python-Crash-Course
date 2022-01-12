def build_profile(first, last, **user_info) -> dict:
    """Build a dictionary containing everything we know about a user."""
    
    user_info['first_name'] = first
    user_info['last_name'] = last
    return f'\n{user_info}\n'

user_profile = build_profile('William', 'Jaber', age = 27,
                location = 'South America', field = 'Programming')

print(user_profile)
