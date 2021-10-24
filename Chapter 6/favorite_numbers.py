favorite_numbers = {
    'kari': 1,
    'dave': 2,
    'dan': 3,
    'alex': 4,
    'edd': 5,
    }


for keys in favorite_numbers:
    print(keys)

for values in favorite_numbers:
    print(favorite_numbers[values])

for k, v in favorite_numbers.items():
    print(f'{k}: {v}')

# print(favorite_numbers.items())
