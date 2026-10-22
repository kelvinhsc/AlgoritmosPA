numeros = []

for i in range(5):
    numero = int(input("Digite um valor: "))
    numeros.append(numero)

print("Ordem digitada:")

for i in range(5):
    print(numeros[i])

print("Ordem inversa:")

for i in range(4, -1, -1):
    print(numeros[i])