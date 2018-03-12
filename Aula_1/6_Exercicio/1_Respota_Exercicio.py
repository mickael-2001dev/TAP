def retorna_valor_imposto_renda(salario_anual):
    if (salario_anual < 22847.76):
        return 0
    elif 22847.77 < salario_anual < 33919.80:
        return salario_anual * 0.075
    elif 33919.81 < salario_anual < 45012.60:
        return salario_anual * 0.15
    elif 45012.61 < salario_anual <= 55976.16:
        return salario_anual * 0.225
    else: return salario_anual * 0.275

def calcula_media_salarial(soma_total_salario, numero_max_meses):
    return soma_total_salario_anual / numero_max_meses

def retorna_nome__completo(nome, sobrenome):
    return nome + " " + sobrenome

def imprimir_informacoes_empregado(nome_funcionario, salario_anual, media_salarial, imposto_renda):
    print("Funcionario: " + str(nome_funcionario))
    print("Valor total salario anual: " + str(salario_anual))
    print("Media salarial: " + str(media_salarial))
    print("Imposto de Renda: " + str(imposto_renda))

def retornar_nome_mes(numero_mes):
    if numero_mes == 1:
        return "Janeiro"
    elif numero_mes == 2:
        return "Fevereiro"
    elif numero_mes == 3:
        return "Marco"
    elif numero_mes == 4:
        return "Abril"
    elif numero_mes == 5:
        return "Maio"
    elif numero_mes == 6:
        return "Junho"
    elif numero_mes == 7:
        return "Julho"
    elif numero_mes == 8:
        return "Agosto"
    elif numero_mes == 9:
        return "Setembro"
    elif numero_mes == 10:
        return "Outubro"
    elif numero_mes == 11:
        return "Novembro"
    elif numero_mes == 12:
        return "Dezembro"
    else:
        return "Mes nao encontrado"


nome_funcionario = input("Digite o nome do funcionario: ")
sobrenome_funcionario = input("Digite o sobrenome do funcionario: ")
nome_completo_funcionario = retorna_nome__completo(nome_funcionario, sobrenome_funcionario)

numero_mes = 1;
numero_max_meses = 12
soma_total_salario_anual = 0

while (numero_mes <= numero_max_meses):
    try:
        valor_salario_mensal = input(
            "Entre o valor do salario correspondente ao mes de  " + retornar_nome_mes(numero_mes) + ": ")
        valor_salario_mensal = int(valor_salario_mensal)
        soma_total_salario_anual += valor_salario_mensal
        numero_mes = numero_mes + 1
    except:
        print("Valor informado invalido")

media_salarial = calcula_media_salarial(soma_total_salario_anual, numero_max_meses)
imposto_de_renda_pago = retorna_valor_imposto_renda(soma_total_salario_anual);
imprimir_informacoes_empregado(nome_completo_funcionario, soma_total_salario_anual, media_salarial, imposto_de_renda_pago)
