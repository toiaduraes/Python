#Programa que leia vários números inteiros pelo teclado.
#O programa vai parar quando o usuário digitar o valor 999, que é a condição de parada.
#No final, mostre quantos números foram digitados e qual foi a soma entre eles.
#Desconsiderando o flag.

n = int(input('Digite um número:'))
count = 1
n2 = 0
while n != 999:
    n2 += n
    count += 1
    n = int(input('Digite outro número:'))
print (f'A soma entre os números digitados foi de: {n2}, A quantidade de número digitados foi de: {count}')

