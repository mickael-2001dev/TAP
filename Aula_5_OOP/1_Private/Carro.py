# Como declarar um método ou atributo privado
# Programando o comportamento da classe
class Carro():
    def __init__(self):
        self.__rodas = 4
        self.ligado = False

    def __dar_partida(self):
        self.ligado = True

    def dar_partida_automatica(self):
        self.ligado = True

    def desligar(self):
        self.ligado = False

    def abrir_porta_malas(self):
        if (self.ligado == True):
            print("Carro ligado não é possível abrir o porta malas")
        else:
            print("Porta malas aberto")

c = Carro()
c.dar_partida_automatica()
c.abrir_porta_malas()
c.desligar()
c.abrir_porta_malas()






