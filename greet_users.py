def greet_users(names):
    """ask a simple greet to everyone in the list"""
    for name in names:
        msg = "Hello, " + name.title() + "!"
        print (msg)

usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)