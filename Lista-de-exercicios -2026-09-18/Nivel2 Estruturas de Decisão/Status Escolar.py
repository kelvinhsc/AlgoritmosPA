nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

media = (nota1 + nota2) / 2

print(f"Média: {media:.1f}")

if media >= 7:
    print("APROVADO")
elif media >= 5:
    print("RECUPERAÇÃO")
else:
    print("REPROVADO")