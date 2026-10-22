notas = []
soma = 0

for i in range(5):
    nota = float(input("Digite a nota do aluno: "))
    notas.append(nota)
    soma += nota

media = soma / 5
quantidade = 0

for nota in notas:
    if nota > media:
        quantidade += 1

print("Média da turma:", media)
print("Alunos acima da média:", quantidade)