class Carro():
    def __init__(self, numero_rodas):
        self.__rodas = numero_rodas
        self.ligado = False

    def __dar_partida(self):
        self.ligado = True

    def dar_partida_automatica(self):
        self.__dar_partida()

    def desligar(self):
        self.ligado = False

    def print_info(self):
        print("Número rodas",self.__rodas)
        print("Ligado",self.ligado)


# Exemplo de como aplicar herança
class Carro_Luxo(Carro):
    def dar_partida_eletrica(self):
        self.dar_partida_automatica()



################## Execution
cl = Carro_Luxo(4)
cl.dar_partida_automatica()
cl.print_info()
