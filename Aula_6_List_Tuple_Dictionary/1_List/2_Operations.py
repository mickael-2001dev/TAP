lista = ['José','Maria','Alberto','Roberto']

lista.append('Leonardo')

print(lista)

lista.insert(1,'Marcia')

print(lista)

lista.extend(['Claudia','Marcelo','Cecilia'])

print(lista)

#como saber o index de um elemento

print(lista.index('Claudia'))


#buscando se um elemento existe

existe = "Claudia" in lista;

print(existe)

#eliminando

lista.remove('Claudia')

print(lista)


#elimina último elemento da lista

lista.pop()

print(lista)

#união de listas

lista2 = ['Maradona','Pelé','Roberto Carlos']

lista3 = lista + lista2

print(lista3)


#multiplicando uma lista

listaMultiplicada = lista * 3

print(listaMultiplicada)

















