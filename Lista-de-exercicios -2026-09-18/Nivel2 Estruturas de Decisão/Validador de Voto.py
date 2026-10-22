idade = int(input("Digite sua idade: "))

if idade < 16:
    print("Não vota.")
elif idade >= 16 and idade <= 17 or idade > 65:
    print("Voto facultativo.")
else:
    print("Voto obrigatório.")