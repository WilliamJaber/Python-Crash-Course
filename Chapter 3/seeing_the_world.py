fav_places = ['Hong Kong', 'New york', 'Miami', 'London', 'Milan']

print(fav_places)

# Using sorted()
print(sorted(fav_places))

# list is still in its original order by printing it again.
print(fav_places)

# Using reverse()
fav_places.reverse()
print(fav_places)

# Using reverse() to change the order of the list again.
fav_places.reverse()
print(fav_places)

# Using sort() to change the list permanently so it’s stored in alphabetical order.
fav_places.sort()
print(fav_places)

# Using sort() to change the list so it’s stored in reverse alphabetical order.
fav_places.sort(reverse=True)
print(fav_places)
