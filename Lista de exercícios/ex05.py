#Faça um programa que leia um caractere e indique se é uma vogal ou consoante.

letra = input('Digite uma letra para testar se é vogal ou consoante:').lower()

if letra in 'aeiou':
    print('A letra é uma vogal')
else:
    print('A letra é uma consoante')
