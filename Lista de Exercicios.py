funcionarios = []
resultados = []

# Leitura dos funcionários
for i in range(10):
    nome = input("Digite o nome: ")
    salario = float(input("Digite o salário bruto: "))
    genero = input("Digite o gênero (M/F): ")

    funcionarios.append([nome, salario, genero])

# Cálculos
for i in range(10):
    inss = funcionarios[i][1] * 0.11
    fgts = funcionarios[i][1] * 0.05

    salario_liquido = funcionarios[i][1] - inss - fgts

    if salario_liquido < 7298.97:
        vale = 729.87
    else:
        vale = 499.78

    total = salario_liquido + vale

    resultados.append([salario_liquido, vale, total])


qtd_masculino = 0
qtd_feminino = 0

maior_salario = resultados[0][0]
menor_salario = resultados[0][0]

maior_masculino = 0
maior_feminino = 0

# Busca dos resultados nas matrizes
for i in range(10):

    if funcionarios[i][2].upper() == "M":
        qtd_masculino += 1

        if resultados[i][0] > maior_masculino:
            maior_masculino = resultados[i][0]

    if funcionarios[i][2].upper() == "F":
        qtd_feminino += 1

        if resultados[i][0] > maior_feminino:
            maior_feminino = resultados[i][0]

    if resultados[i][0] > maior_salario:
        maior_salario = resultados[i][0]

    if resultados[i][0] < menor_salario:
        menor_salario = resultados[i][0]


# Exibição
for i in range(10):
    print("\nNome:", funcionarios[i][0])
    print("Salário líquido: R$", round(resultados[i][0], 2))
    print("Vale alimentação: R$", round(resultados[i][1], 2))
    print("Salário líquido + vale: R$", round(resultados[i][2], 2))

print("\nFuncionários masculinos:", qtd_masculino)
print("Funcionários femininos:", qtd_feminino)
print("Maior salário líquido: R$", round(maior_salario, 2))
print("Menor salário líquido: R$", round(menor_salario, 2))
print("Maior salário líquido masculino: R$", round(maior_masculino, 2))
print("Maior salário líquido feminino: R$", round(maior_feminino, 2))