current_users = {'vodka', 'duke', 'jack', 'josh', 'lucy'}

new_users = {'duke', 'josh'}

for check_users in current_users:
    if check_users in new_users:
        print ( check_users + " has been uesd,you can't use this name")
    else:
        print ("You can use this name")