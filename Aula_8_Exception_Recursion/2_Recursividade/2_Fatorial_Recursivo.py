def fatorial(numero):
    if numero == 1:
        return 1
    return numero * fatorial(numero-1)

numero_entrado = int(input("Digite um número:"))

print(fatorial(numero_entrado))