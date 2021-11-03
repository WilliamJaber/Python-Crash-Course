prompt = "\nEnter the Topping you'd like to add for your pizza:"
prompt += "\nor enter 'quit' to end the program.\n"

topping = ""
while topping != 'quit':
    topping = input(prompt)
    if topping != 'quit':
        print(f'You’ll add {topping} to the pizza.')
