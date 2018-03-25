print("Calculadora de Média")
print("Entre com as notas do aluno.")

nome_aluno = input("Digite o nome do aluno: ")

num_materias = 0;

total_pontos = 0;

done = False;

while not done:
    nota = input("Digite a nota:")
    if nota == '':
        done = True
    else:
        nota = int(nota)
        num_materias+=1
        total_pontos+=nota

if num_materias > 0:
    media = total_pontos / num_materias
    print("Aluno: "+nome_aluno+" sua média é = "+str(media))
