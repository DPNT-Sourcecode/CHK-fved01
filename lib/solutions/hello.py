

# noinspection PyUnusedLocal
# friend_name = unicode string
def hello(friend_name):
    if friend_name.lower() == 'john':
        return 'Hello, {}'.format(friend_name)

    return 'Hello, World!'
