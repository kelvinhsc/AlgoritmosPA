votos = [0, 0, 0, 0, 0]

while True:
    voto = int(input("Digite seu voto (0 encerra): "))

    if voto == 0:
        break

    if voto >= 1 and voto <= 5:
        votos[voto - 1] += 1
    else:
        print("Voto inválido")

print("João:", votos[0], "votos")
print("Maria:", votos[1], "votos")
print("José:", votos[2], "votos")
print("Nulos:", votos[3])
print("Brancos:", votos[4])

maior = max(votos[0:3])

if votos[0] == votos[1] == votos[2]:
    print("Empate entre os candidatos")
elif votos[0] == maior and votos[1] == maior or votos[0] == maior and votos[2] == maior or votos[1] == maior and votos[2] == maior:
    print("Empate entre os candidatos")
elif votos[0] == maior:
    print("João venceu")
elif votos[1] == maior:
    print("Maria venceu")
else:
    print("José venceu")