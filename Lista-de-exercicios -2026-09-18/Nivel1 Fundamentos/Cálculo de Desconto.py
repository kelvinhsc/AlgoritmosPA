valor = float(input("Digite o valor do produto: "))

desconto = valor * 0.15
valor_final = valor - desconto

print(f"Desconto: R$ {desconto:.2f}")
print(f"Valor com desconto: R$ {valor_final:.2f}")