nomes = []
notas = []

for i in range(3):
    nome = input("Nome do aluno: ")
    nota = float(input("Nota do aluno: "))

    nomes.append(nome)
    notas.append(nota)

for i in range(3):
    print("Nome:", nomes[i])
    print("Nota:", notas[i])

    if notas[i] >= 7:
        print("Aprovado")
    else:
        print("Reprovado")