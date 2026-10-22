senha_correta = "etec123"

senha = input("Digite a senha: ")

while senha != senha_correta:
    print("Senha incorreta!")
    senha = input("Digite a senha novamente: ")

print("Acesso Permitido.")