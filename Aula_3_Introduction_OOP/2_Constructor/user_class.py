class User:

    def __init__(self, login, password):
        self.login = login
        self.password = password


# Constructing a user
user = User("login1","password1")
print("User: "+user.login+" "+"Password: "+user.password)



