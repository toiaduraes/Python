# Escreva um programa que leia um número N inteiro qualquer e
# mostre na tela os N primeiros elementos de uma Sequência de Fibonacci.

n1 = int(input('Digite o primeiro termo da sequencia de Fibonnaci:'))
n2 = int(input('Digite o segundo termo da sequencia de Fibonnaci:'))
qtd = int(input('Deseja ver quantos termos da sequencia?'))
n3 = 0
n4 = 0
#count = (qtd - 2)/4
print (f'{n1} , {n2}')
while qtd != 0:
    n3 = n1 + n2
    print (f'{n3} ->', end ='')
    n4 = n2 + n3
    print (f'{n4} ->', end ='')
    n1 = n3 + n4
    print (f'{n1}->', end ='')
    n2 = n4 + n1
    print (f'{n2}->', end ='')
    qtd -= 1
