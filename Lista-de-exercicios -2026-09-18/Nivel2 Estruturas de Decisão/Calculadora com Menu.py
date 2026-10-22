numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

print("\n1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")

opcao = int(input("Escolha uma operação: "))

if opcao == 1:
    resultado = numero1 + numero2
    print("Resultado:", resultado)

elif opcao == 2:
    resultado = numero1 - numero2
    print("Resultado:", resultado)

elif opcao == 3:
    resultado = numero1 * numero2
    print("Resultado:", resultado)

elif opcao == 4:
    if numero2 != 0:
        resultado = numero1 / numero2
        print("Resultado:", resultado)
    else:
        print("Não é possível dividir por zero.")

else:
    print("Opção inválida.")