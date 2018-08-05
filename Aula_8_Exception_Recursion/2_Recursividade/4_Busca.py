from random import *
import time

numeros = []

for v in range(1, 10000000):
    numeros.append(randint(1, 10000000))

numeros.sort()
print(numeros[950000])


num = int(input("Digite o número:"))
tempo_inicial = int(round(time.time() * 1000))

for v in numeros:
    if v == num:
        print("Existe:", num)
        break

tempo = (int(round(time.time() * 1000)) - tempo_inicial)
print("Tempo", tempo)







