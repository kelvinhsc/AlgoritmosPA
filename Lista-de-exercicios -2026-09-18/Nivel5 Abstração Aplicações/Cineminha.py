poltronas = [False] * 10

while True:
    print("\nMapa das poltronas:")
    for i in range(10):
        if poltronas[i]:
            print(i, "- Ocupada")
        else:
            print(i, "- Livre")

    numero = int(input("Poltrona para reservar (-1 para sair): "))

    if numero < 0:
        break

    if numero > 9:
        print("Poltrona inválida!")
    elif poltronas[numero]:
        print("Ocupada!")
    else:
        poltronas[numero] = True
        print("Reservada!")