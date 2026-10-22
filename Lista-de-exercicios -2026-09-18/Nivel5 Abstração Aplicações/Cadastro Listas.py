nomes = []
idades = []

while True:
    print("\n1 - Cadastrar")
    print("2 - Listar maiores de 18 anos")
    print("3 - Sair")

    opcao = input("Escolha: ")

    if opcao == "1":
        nome = input("Nome: ")
        idade = int(input("Idade: "))

        nomes.append(nome)
        idades.append(idade)

        print("Cadastro realizado!")

    elif opcao == "2":
        for i in range(len(nomes)):
            if idades[i] >= 18:
                print(nomes[i], "-", idades[i], "anos")

    elif opcao == "3":
        break

    else:
        print("Opção inválida!")