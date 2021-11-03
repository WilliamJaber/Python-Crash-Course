prompt = "\nEnter the Topping you'd like to add for your pizza:"
prompt += "\nor enter 'quit' to end the program.\n"

# Conditional test in the while statement to stop the loop.
topping = ""
while topping != 'quit':
    topping = input(prompt)
    if topping != 'quit':
        print(f'You’ll add {topping} to the pizza.')

# Use an active variable to control how long the loop runs.
preparing = True
while preparing:
    user_input = input(prompt)
    if user_input == 'quit':
        preparing = False
    else:
        print(f'You’ll add {user_input} to the pizza.')

# Use a break statement to exit the loop when the user enters a 'quit' value.
toppings = []
while True:
    user_input = input(prompt)
    if user_input == 'quit':
        break
    else:
        toppings.append(user_input)
        print(toppings)
