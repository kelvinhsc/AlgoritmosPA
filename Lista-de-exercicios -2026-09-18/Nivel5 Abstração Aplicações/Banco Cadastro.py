nome = ""
conta = ""
saldo = 0
criada = False

while True:
    print("\n1 - Criar Conta")
    print("2 - Depositar")
    print("3 - Sacar")
    print("4 - Extrato/Ver Saldo")
    print("5 - Sair")

    opcao = input("Escolha: ")

    if opcao == "1":
        if criada:
            print("A conta já foi criada!")
        else:
            nome = input("Nome: ")
            conta = input("Número da conta: ")
            saldo = 0
            criada = True
            print("Conta criada com sucesso!")

    elif opcao == "2":
        if criada:
            valor = float(input("Valor do depósito: R$ "))

            if valor > 0:
                saldo += valor
                print("Depósito realizado!")
            else:
                print("Valor inválido!")
        else:
            print("Crie uma conta primeiro!")

    elif opcao == "3":
        if criada:
            valor = float(input("Valor do saque: R$ "))

            if valor > 0 and valor <= saldo:
                saldo -= valor
                print("Saque realizado!")
            else:
                print("Saldo insuficiente ou valor inválido!")
        else:
            print("Crie uma conta primeiro!")

    elif opcao == "4":
        if criada:
            print("Titular:", nome)
            print("Conta:", conta)
            print("Saldo: R$", round(saldo, 2))
        else:
            print("Crie uma conta primeiro!")

    elif opcao == "5":
        print("Obrigado por utilizar o banco!")
        break

    else:
        print("Opção inválida!")