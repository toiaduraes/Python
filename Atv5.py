#Faça um programa que leia um número inteiro e mostre na tela
#O seu sucessor e o seu antecessor

numero = int(input('Qual o número você quer saber o antecessor e sucessor?'))

a = numero - 1
s = numero + 1

print('O Antecessor do {} é {} \nO Sucessor do {} é {}'.format(numero, a, numero, s))