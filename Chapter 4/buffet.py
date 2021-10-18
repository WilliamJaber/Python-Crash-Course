buffet_food = ('pasta', 'salad', 'chicken', 'beef', 'sandwich')

for food in buffet_food:
    print(food)

# try to modify on of the items, and make sure python rejects the change.
print(f'\n{buffet_food[0]}')

# TypeError: 'tuple' object does not support item assignment
buffet_food[0] = 'turkey'
print(f'\n{buffet_food[0]}')

# reassigning a variable is valid
buffet_food = ('TURKEY', 'TUNA', 'chicken', 'beef', 'sandwich')
for food in buffet_food:
    print(food)
