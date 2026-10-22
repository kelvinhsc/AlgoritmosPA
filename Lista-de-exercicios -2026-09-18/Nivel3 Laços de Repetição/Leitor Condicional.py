quantidade = 0
soma = 0

numero = int(input("Digite um número (0 para parar): "))

while numero != 0:
    quantidade += 1
    soma += numero

    numero = int(input("Digite outro número (0 para parar): "))

print("Quantidade de números:", quantidade)
print("Soma dos números:", soma)