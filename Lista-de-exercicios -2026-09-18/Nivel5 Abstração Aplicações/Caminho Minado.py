import random

caminho = [0] * 10
minas = random.sample(range(10), 3)

for mina in minas:
    caminho[mina] = 1

passos = []

for i in range(5):
    posicao = int(input("Escolha uma posição de 0 a 9: "))

    if posicao < 0 or posicao > 9 or posicao in passos:
        print("Posição inválida ou já escolhida!")
        continue

    passos.append(posicao)

    if caminho[posicao] == 1:
        print("Você pisou em uma mina! Fim de jogo.")
        break

    print("Caminho livre!")

else:
    print("Parabéns! Você sobreviveu aos 5 passos!")