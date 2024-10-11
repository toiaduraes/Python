# Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário.
# O programa será interrompido quando o número solicitado for negativo.

while True:
    num = int(input('Qual o número deseja ver a tabuada?'))
    if num < 0:
        print('Fim do programa!')
        break
    print (f'A tabuada do número {num} é:')
    for c in range (0,11):
        print (f'{num} x {c} = {num*c}')
