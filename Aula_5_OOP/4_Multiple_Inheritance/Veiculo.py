class Bicicleta():
    numero_rodas=2
    numero_marchas=21

    def __init__(self, rodas):
        self.numero_rodas = rodas

    def pedalar(self):
        print("Pedalando")

class VEletrico():
    total_autonomia=100
    cargado=True

    def __init__(self, autonomia):
        self.total_autonomia = autonomia

    def cargar(self):
        self.cargado = True
        print("Cargado =",self.cargado)

# Exemplo de herança múltipla
# Quando existir herança muúcicleta,VEletrico):
    pass


# Test


be = Bicicleta_Eletrica(2)
be.cargar()
be.pedalar()
