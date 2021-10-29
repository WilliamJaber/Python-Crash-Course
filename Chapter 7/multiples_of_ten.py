user_input = input('Insert a number:\n')
user_input = int(user_input)

if user_input % 10 == 0:
    print('Your number is multiple of ten.')
else:
    print('Sorry, your number is not multiple of ten.')
