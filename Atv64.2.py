# Escreva um programa que leia um número N inteiro qualquer e
# Mostre na tela os N primeiros elementos de uma Sequência de Fibonacci.

n1 = int(input('Digite o primeiro termo da sequência:'))
n2 = int (input('Digite o segundo termo da sequência:'))
qtd = int(input('Deseja ver quantos elementos?'))
count = 0
n3 = 0
print (f'Os primeiros {qtd} elementos são:{n1},{n2}', end='')
while count < (qtd-2):
    n3 = n1 +n2
    print(f',{n3}', end='')
    n1 = n2
    n2 = n3
    count += 1