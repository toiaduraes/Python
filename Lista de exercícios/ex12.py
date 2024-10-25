#Verificar código de usuário e senha:

codigo_correto = 1234
senha_correta = 9999

codigo = int(input("Digite o código:"))

if codigo != codigo_correto:
    print("Código inválido.")
    codigo = int(input("Digite o código:"))
else:
    senha = int(input("Digite a senha:"))

    if senha != senha_correta:
        print("senha inválida.")
        senha = int(input("Digite a senha:"))
    else:
        print("Acesso permitido.")