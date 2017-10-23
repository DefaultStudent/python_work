users_list = {'josh', 'simon', 'jack', 'rose', 'admin'}

user = "admin"

if users_list :
    for users in users_list:
        if users in user:
            print ("Hello " + users + ",would you like to see a status report?")
        else:
            print ("Hello " + users + ",thank you for logging in again")
else:
    print ("We need some users")