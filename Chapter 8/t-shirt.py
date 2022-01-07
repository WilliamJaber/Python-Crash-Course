def make_shirt(size, message):
    print(f'This shirt is size: {size}, and has a message: {message}.')

# positional arguments
make_shirt('S', 'Style has no size')
# keyword arguments
make_shirt(size = 'S', message = 'Style has no size')
