
class User(object):

    username = ""
    password = ""

    def __init__(self, username, password):
        self.username = username
        self.password = password

def make_account(username, password):
    user = User()
    user.username = raw_input("username: ")
    user.password = raw_input("password: ")
    return user

def creating_global_input():
    user.username = globals(username)
    user.password = globals(password)
#
# username = raw_input("username: ")
# password = raw_input("password: ")
# print(username)

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


# #lcreate_account()
# # sp2 = raw_input("Enter Password ")
