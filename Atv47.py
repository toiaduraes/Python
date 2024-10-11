#Programa que mostre na tela todos os números pares que estão no intervalo de 1 e 50.

for c in range (1,51):
    if c%2 == 0: #resto da divisão, se o número c dividido por 2, tiver resto 0, então é par.
        print (f'{c}')