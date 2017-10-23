current_users = ['vodka', 'duke', 'jack', 'josh', 'lucy']

new_users = ['duke', 'JOSH']

for check_users in current_users:
    if check_users in new_users:
        print (check_users + " has been used")
    elif check_users.upper() in new_users:
        print (check_users.upper() + " is not good")
    else:
        print (check_users + " is ok")