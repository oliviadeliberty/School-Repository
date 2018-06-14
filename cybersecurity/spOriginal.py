

username = raw_input("username: ")
password = raw_input("password: ")
print(username)

def standardPassword():
    username_input = raw_input("username: ")
    if username_input == username:
        password_input = raw_input("password: ")
        if password_input == password:
            print("access granted")
        else:
            print("incorrect password")
            standardPassword()
    else:
        print("No account by that name")
        standardPassword()

standardPassword()