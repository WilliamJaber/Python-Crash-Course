sandwich_orders = ['pastrami', 'tuna', 'pastrami', 'focaccia', 'roastbeef', 'pastrami']
finished_sandwiches = []

print('\nThe Deli has run out of pastrami.')
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

for sandwich in sandwich_orders:
    finished_sandwiches.append(sandwich.title())
print(f'\nVerify your order:\n{finished_sandwiches}')
