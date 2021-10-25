favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

# Make a list of people who should take the favorite languages poll.
# Include some names that are already in the dictionary and some that are not.
people = ['greg', 'sarah', 'dave', 'phil']

# Loop through the list of people who should take the poll.
# If they have already taken the poll, print a message thanking them for responding.
# If they have not yet taken the poll, print a message inviting them to take the poll.
for name in people:
    if name in favorite_languages.keys():
        print(f'Hey {name.title()}, thanks for responding the poll.')
    else:
        print(f'Hello {name.title()}, you are invited to take the poll let us know what is your favorite language!')
