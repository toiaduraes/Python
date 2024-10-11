# Crie um programa que leia a idade e o sexo de várias pessoas.
# A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
# A) quantas pessoas tem mais de 18 anos.
# B) quantos homens foram cadastrados.
# C) quantas mulheres tem menos de 20 anos.
f=m=p=0
condicao = 0
while True:
    sexo = str(input('Qual o sexo da pessoa, [F/M]:')).strip().upper()
    idade = int(input('Qual a idade da pessoa:'))
    if idade > 18:
        p += 1
    if sexo == 'M':
        m += 1
    if sexo == 'F' and idade < 20:
        f += 1
    condicao = int(input('Deseja continuar? [1] para sim e [2] para não:'))
    if condicao == 2:
        break

print(f'{p} Pessoa(s) tem mais de 18 anos, {m} homem(s) cadastrado(s) e {f} mulhere(s) tem menos de 20 anos.')