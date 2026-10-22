produtos = []
quantidades = []

while True:
    print("\n1 - Adicionar Produto")
    print("2 - Dar Baixa")
    print("3 - Ver Estoque")
    print("4 - Sair")

    opcao = input("Escolha: ")

    if opcao == "1":
        nome = input("Nome do produto: ")
        quantidade = int(input("Quantidade: "))

        if nome in produtos:
            i = produtos.index(nome)
            quantidades[i] += quantidade
        else:
            produtos.append(nome)
            quantidades.append(quantidade)

        print("Produto adicionado!")

    elif opcao == "2":
        nome = input("Produto: ")

        if nome in produtos:
            i = produtos.index(nome)
            quantidade = int(input("Quantidade para retirar: "))

            if quantidade > 0 and quantidades[i] >= quantidade:
                quantidades[i] -= quantidade
                print("Baixa realizada!")
            else:
                print("Estoque insuficiente ou quantidade inválida.")
        else:
            print("Produto não encontrado!")

    elif opcao == "3":
        for i in range(len(produtos)):
            print(produtos[i], "-", quantidades[i], "unidades")

    elif opcao == "4":
        break

    else:
        print("Opção inválida!")