from random import *
import time
import sys

def binary_search(data, buscando, low, high):
    if low > high:
        return False
    else:
        mid = (high + low) // 2

        if data[mid] == buscando:
            return True
        elif buscando < data[mid]:
            return binary_search(data, buscando, low, mid)
        else:
            return binary_search(data, buscando, mid+1, high)


numeros = []
sys.setrecursionlimit(100000000)

for v in range(1, 10000000):
    numeros.append(randint(1, 10000000))
numeros.sort()

print(numeros)
num_buscado = int(input("Digite o número:"))

tempo_inicial = int(round(time.time() * 1000))
print(tempo_inicial)

result = binary_search(numeros, num_buscado, 0, len(numeros)-1)

print("Existe:", result)
print(int(round(time.time() * 1000)))
tempo = (int(round(time.time() * 1000)) - tempo_inicial)
print(tempo)

