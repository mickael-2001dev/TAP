class Veiculos():
    def movimentar(self):
        print("Movimentação ...... ")

class Bicicleta(Veiculos):
    def movimentar(self):
        print("Movendo bicicleta")

class Aviao(Veiculos):
    def movimentar(self):
        print("Movendo aviao")

class Carro(Veiculos):
    def movimentar(self):
        print("Movendo carro")


# Exemplo de polimorfismo
def movimentar(veiculo):
    veiculo.movimentar()


o = Bicicleta()
movimentar(o)

o = Aviao()
movimentar(o)


o = Carro()
movimentar(o)