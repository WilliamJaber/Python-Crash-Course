guest_list = ['Greg', 'Alex', 'Dan', 'Sam', 'Dave', 'Eddy']

print('I am so sorry, due to the restaurant politics I can only invite two guests for dinner.')

print(guest_list)

guest_list.pop()
guest_list.pop()
guest_list.pop()
guest_list.pop()

print(f'{guest_list[0]} you still invited for my celebration dinner.')
print(f'{guest_list[1]} you still invited for my celebration dinner.')

del guest_list[0]
del guest_list[0]

print(guest_list)
