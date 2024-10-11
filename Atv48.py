#programa que calcule a soma entre todos os números ímpares que são múltiplos de três
#que se encontram no intervalo de 1 a 500.
m = 0
for c in range(1,500):
    if c%2 == 1 and c%3 == 0:
        m = m + c
        print (f'Valor de c: {c}, soma dos múltiplos: {m}')
