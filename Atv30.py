#Programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.

num = float(input('Qual o número deseja saber se é par ou ímpar?'))

if ((num%2) == 0 ):
    print ('O número é par.')
else:
    print('O número é ímpar.')