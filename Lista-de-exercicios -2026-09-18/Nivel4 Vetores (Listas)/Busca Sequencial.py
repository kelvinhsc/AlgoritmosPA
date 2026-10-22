numeros = []

for i in range(8):
    numero = int(input("Digite um número: "))
    numeros.append(numero)

busca = int(input("Digite o número que deseja buscar: "))
encontrou = False

for i in range(len(numeros)):
    if numeros[i] == busca:
        print("Número encontrado na posição", i)
        encontrou = True

if not encontrou:
    print("Número não encontrado")