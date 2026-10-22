valor = int(input("Digite o valor do saque: "))

notas = [20, 10, 5, 2, 1]

for nota in notas:
    quantidade = valor // nota
    valor = valor % nota

    if quantidade > 0:
        print(quantidade, "nota(s) de R$", nota)