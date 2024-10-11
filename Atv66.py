  #Programa que leia vários números inteiros.
#No final da execução, mostre a média entre todos os valores e
#Qual foi o MAIOR e qual foi o MENOR entre os valores lidos.
#O programa deve digitar se o usuário quer ou não continuar a digitar os valores.

n = int(input('Digite um número:'))
condicao = 's'
media = n2 = 0
n_m = n_M = n
count = 1
while condicao == 's':
    if n > n_M:
        n_M = n
        print(f'Valor de n_M (valor maior): {n_M}')
    if n < n_m:
        n_m = n
        print(f'Valor de n_m (valor menor): {n_m}')
    condicao = str(input('Deseja continuar a digitar? [s/n]'))
    n2 += n
    if condicao == 's':
        n = int(input('Digite um número:'))
        count += 1
    elif condicao == 'n':
        print('Fim do programa!')
    while condicao != 's' and condicao != 'n':
        print('Você digitou o comando errado! Deve ser *s* para sim e *n* para não. ')
        condicao = str(input('Deseja continuar a digitar? [s/n]'))

media = n2 / count
print (f'A média foi de: {media}, O maior valor foi: {n_M}, O menor valor foi:{n_m}')

