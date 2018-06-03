class Estado:
    def __init__(self, nome, uf, nome_governador, orcamento_anual, ):
        self.__nome = nome
        self.__uf = uf
        self.__nome_governador = nome_governador
        self.__orcamento_anual = orcamento_anual
        self.__total_habitantes = 0
        self.__lista_municipios = {}

    def incluir_municipio(self,nome, habitantes, superficie):
        if self.__lista_municipios.get(nome) is None:
            self.__total_habitantes = self.__total_habitantes + habitantes
            municipio = {"nome": nome, "habitantes": habitantes, "superficie": superficie, "orcamento_anual": 0}
            self.__lista_municipios[nome] = municipio

    def total_habitantes(self):
        return self.__total_habitantes

    def distribuir_orcamento(self):
        for municipio in self.__lista_municipios.values():
            habitantes_municipio = int(municipio["habitantes"])
            orcamento = (habitantes_municipio * self.__orcamento_anual) / self.__total_habitantes
            municipio["orcamento_anual"] = orcamento

    def menor_municipio(self):
        pass

    def maior_municipio(self):
        pass

estado = Estado("Rio Grande do Sul","RS","Olivio Dutra",1000000)
estado.incluir_municipio("Livramento",1000,1000)
estado.incluir_municipio("Livramento",1000,1000)
estado.incluir_municipio("Livramento2",1000,100)
estado.incluir_municipio("Livramento3",1000,45100)
print(estado.total_habitantes())
estado.distribuir_orcamento()
print(estado.menor_municipio())