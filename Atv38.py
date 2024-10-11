#Programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:
#O primeiro valor é maior
#O segundo valor é maior
#Não existe valor maior, os dois são iguais.

num1 = float(input('Primeiro número:'))
num2 = float(input('Segundo número:'))

if num1 > num2:
    print('O primeiro valor é maior.')
elif num2 > num1:
    print('O segundo número é maior.')
else:
    print('Os dois são iguais.')