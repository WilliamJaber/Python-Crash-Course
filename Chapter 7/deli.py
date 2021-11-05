sandwich_orders = ['tuna', 'focaccia', 'roastbeef']
finished_sandwiches = []

while sandwich_orders:
        made = sandwich_orders.pop()
        print(f'\n{made.title()} sandwich is in process....')
        finished_sandwiches.append(made)

print('\nYour order is complete:')
for sandwich in finished_sandwiches:
    print(sandwich.title())
