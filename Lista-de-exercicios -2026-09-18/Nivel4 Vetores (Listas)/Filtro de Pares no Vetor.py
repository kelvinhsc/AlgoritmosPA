numeros = []

for i in range(10):
    numero = int(input("Digite um número: "))
    numeros.append(numero)

for numero in numeros:
    if numero % 2 == 0:
        print(numero)