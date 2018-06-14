class users(object):
    def ___init___(self, user, password):
        self.user = 'Jamie'
        self.password = 'cats'

    def passwordInput(usernameInput, passwordInput):
            usernameCheck = usernameInput == self.user
            passwordCheck = passwordInput == self.password
            if usernameCheck == True:
                print "Password?"
                if passwordInput == True:
                    "Access Granted"
                else:
                    "Access Denied"
            else:
                return "Access Denied"


passwordInput('Jamie', 'cats')
