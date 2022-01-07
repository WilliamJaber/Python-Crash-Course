def make_shirt(size = 'L', message = 'I love Python'):
    print(f'This shirt is size: {size}, and has a message: {message}.')


# large shirt and a medium shirt with the default message
make_shirt()
make_shirt(size = 'M')
# shirt of any size with a different message.
make_shirt(size = 'S', message = 'I love Python & You')
