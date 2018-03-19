class User:

    def __init__(self, login, password):
        'Método de inicialização'
        self.login = login
        self.password = password

    def show_info(self):
        'Imprime a informação do usuário'
        print("User:"+self.login+" "+" Password:"+self.password)

    def change_password(self, password):
        'Modifica o password'
        self.password = password


help(User)



