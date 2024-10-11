# Programa que leia uma frase qualquer e diga se ela é um palíndrono desconsiderando os espaços

frase = 'a'
frase_invertida = 'b'

while frase != frase_invertida:
    frase = str(input('Escreva novamente uma frase que gostaria saber se é palíndrono:'))
    frase = frase.replace(' ', '')
    frase_invertida = frase[::-1]
    print(frase_invertida)
    if frase in frase_invertida:
        print(f'A frase é um palíndrono! ')
    else:
        print(f'A frase não é um palíndrono!')