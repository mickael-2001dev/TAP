# Disparando uma exception
# raise ValueError("Valor não pode ser negativo")


def sum_number(number):
    if not isinstance(number, (int, float)):
        raise TypeError('number não é numérico')
    elif number < 0:
        raise ValueError('number é negativo')
    return number + 10


try:
    sum_number("vinte")
except TypeError as e:
    print(e)

try:
    sum_number(-58)
except ValueError as e:
    print(e)

try:
    sum_number("vinte")
except (TypeError, ValueError) as e:
    print(e)

try:
    sum_number("vinte")
except Exception as e:
    print(e)



