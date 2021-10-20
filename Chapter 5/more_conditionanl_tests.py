# Tests for equality and inequality with strings
favorite_food = 'pizza'
print(favorite_food != 'pizza') #False
print(favorite_food == 'pizza') #True

# Tests using the lower() method
client_name = 'John'
print(client_name.lower() == 'john') #True
print(client_name.lower() != 'john') #False

# Numerical tests involving equality and inequality, greater than and less than, greater than or equal to, and less than or equal to
grades = 20
print(grades == 20) #True
print(grades != 20) #False
print(grades < 25) #True
print(grades > 25) #False
print(grades <= 18) #False
print(grades >= 25) #False

# Tests using the and keyword and the or keyword
grade1 = 18
grade2 = 25
print(grade1 >= 20 or grade2 >= 21) #True
print(grade1 >= 20 and grade2 >= 21) #False

# Test whether an item is in a list
my_pizzas = ['pepperoni', 'margarita', 'prosciutto']
print('pepperoni' in my_pizzas) #True
print('salami' in my_pizzas) #False

# Test whether an item is not in a list
print('salami' not in my_pizzas) #True
print('pepperoni' not in my_pizzas) #False
