prompt = "\nTicket price varies according to age, please enter age:\n "

while True:
    age = int(input(prompt))
    if age < 3:
        print('The ticket cost is free.')
    elif age < 12:
        print('Your ticket cost is $10.')
    else:
        print('Your ticket cost is $15.')
