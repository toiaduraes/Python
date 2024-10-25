# Ler o ano atual e o ano de nascimento de uma pessoa. Escrever uma mensagem que diga se ela poderá ou
#não votar este ano (não é necessário considerar o mês em #que a pessoa nasceu)

ano_atual = int(input('Qual o ano atual?'))
nascimento = int(input('Qual o ano do seu nascimento? '))

idade = ano_atual - nascimento

if idade >= 16 :
    print('Você pode votar')
else: 
    print('Você não pode votar')

