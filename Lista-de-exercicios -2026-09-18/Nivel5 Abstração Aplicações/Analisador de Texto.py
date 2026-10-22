frase = input("Digite uma frase: ")

palavras = 0
letras_a = 0
dentro_palavra = False

for letra in frase:
    if letra != " ":
        if not dentro_palavra:
            palavras += 1
            dentro_palavra = True
    else:
        dentro_palavra = False

    if letra == "a" or letra == "A":
        letras_a += 1

print("Quantidade de palavras:", palavras)
print("Quantidade de letras A:", letras_a)