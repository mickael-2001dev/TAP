class Carro():
    ligado = False
    def abrir_porta_malas(self):
        if (self.ligado == True):
            print("Carro ligado não é possível abrir o porta malas")
        else:
            print("Porta malas aberto")

class Carro_Luxo(Carro):
    #Exemplo de como sobrecarregar um método de uma classe pai
    def abrir_porta_malas(self):
        print("Porta malas do carro de luxo aberto")




################## Execution
cl = Carro_Luxo()
cl.abrir_porta_malas()

