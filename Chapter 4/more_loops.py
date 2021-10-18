my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

first_list = []
for food in my_foods:
    first_list.append(food)
print(f'my food:\n {first_list}')

second_list = []
for food in friend_foods:
    second_list.append(food)
print(f'\nfriend food:\n {second_list}')
