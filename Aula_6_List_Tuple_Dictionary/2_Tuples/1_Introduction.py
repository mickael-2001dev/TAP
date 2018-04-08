# as tuplas são imutáveis
# não permite buscar pelo índice
# permite verificar se um elemento existe
# mais rápidas que as listas
# menor espaço em memória


tupla = (200,300,400,500,600)

print(tupla)

valor = tupla[0]

print(valor)

# coversão de uma tupla em lista

lista = list(tupla)

print(lista)

# conversão de uma lista em tuplas

tuplaNova = list(lista)

#verificar se uma elemento existe

existe = 300 in tupla

print(existe)

# método count

print(tupla.count(300))

# método len

print(len(tupla))

# exemplo

minhaTupla = (1,"Alberto","Duque de Caxias 1525")

codigo, nome , endereco = minhaTupla

print(codigo," - ",nome," - ",endereco)


















