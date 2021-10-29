restaurant_seating = input('Good evening, how many people are in you dinner group?\n')
restaurant_seating = int(restaurant_seating)

if restaurant_seating > 8:
    print('Sorry, you will have to wait for a table.')
else:
    print('Of course, your table is ready.')
