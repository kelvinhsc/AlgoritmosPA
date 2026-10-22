numeros = []
pares = []
impares = []

for i in range(10):
    numero = int(input("Digite um número inteiro: "))
    numeros.append(numero)

for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)

print("Lista principal:", numeros)
print("Pares:", pares)
print("Ímpares:", impares)