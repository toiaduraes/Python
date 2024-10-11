#Programa que leia três números e mostre qual é o maior e qual é o menor.

n1 = float(input('Digite o primeiro número:'))
n2 = float(input('Digite o segundo número:'))
n3 = float(input('Digite o terceiro número:'))

lista = [n1,n2,n3]
lista.sort()

print(f'O maior número é: {lista[2]}')
print(f'O menor número é: {lista[0]}')