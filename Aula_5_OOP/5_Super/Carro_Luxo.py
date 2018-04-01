class Carro():
    def __init__(self, ligado):
        self.ligado = ligado

    def show_info(self):
        print("Ligado:",self.ligado)

class Carro_Luxo(Carro):
    def __init__(self, ligado, frigobar):
        super().__init__(ligado)
        self.frigobar = frigobar

    def show_info(self):
        super().show_info()
        print("Friobar:",self.frigobar)



# Exemplo do uso do SUPER
cl = Carro_Luxo(True,True)
cl.show_info()


print(isinstance(cl,Carro_Luxo))
