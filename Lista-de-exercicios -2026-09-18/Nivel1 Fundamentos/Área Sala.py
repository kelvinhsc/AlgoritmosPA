largura = float(input("Digite a largura da sala: "))
comprimento = float(input("Digite o comprimento da sala: "))

area = largura * comprimento
perimetro = 2 * (largura + comprimento)

print(f"Área: {area:.2f} m²")
print(f"Perímetro: {perimetro:.2f} m")