import sys
import time
from random import *


def binary_search(data, numero_buscado, low, high):
    if low > high:
        return False
    else:
        mid = (high + low) // 2

        if data[mid] == numero_buscado:
            return True
        elif numero_buscado < data[mid]:
            return binary_search(data, numero_buscado, low, mid - 1)
        else:
            return binary_search(data, numero_buscado, mid + 1, high)


numeros = [50000]
sys.setrecursionlimit(100000000)

for v in range(1, 10000000):
    numeros.append(randint(1, 10000000))
numeros.sort()

print(numeros)
num_buscado = int(input("Digite o número:"))

tempo_inicial = int(round(time.time() * 1000))
print(tempo_inicial)

result = binary_search(numeros, num_buscado, 0, len(numeros) - 1)

print("Existe:", result)
print(int(round(time.time() * 1000)))
tempo = (int(round(time.time() * 1000)) - tempo_inicial)
print(tempo)
