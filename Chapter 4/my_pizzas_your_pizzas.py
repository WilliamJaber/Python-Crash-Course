my_pizzas = ['pepperoni', 'margarita', 'prosciutto']

friend_pizzas = my_pizzas[:]

# Add a new pizza to the original list.
my_pizzas.append('doble cheese')

# Add a different pizza to the list friend_pizzas.
friend_pizzas.append('salami')

message1 = '\nMy favorite pizzas are: '
print(message1)
for pizza in my_pizzas:
    print(pizza)

message2 = "\nMy friend’s favorite pizzas are: "
print(message2)
for pizza in friend_pizzas:
    print(pizza)
