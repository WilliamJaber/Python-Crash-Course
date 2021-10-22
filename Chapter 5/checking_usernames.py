current_users = ['dave', 'will', 'sara', 'JOE', 'Edd']
new_users = ['liz', 'peter', 'gen', 'joe', 'edd']

lower_case_current_users = []

for user in current_users:
    lower_case_current_users.append(user.lower())
print(lower_case_current_users)

for new_user in new_users:
    if new_user in lower_case_current_users:
        print(f'Sorry! {new_user} is not available, enter a new username')
    else:
        print(f'Great! {new_user} is available')
