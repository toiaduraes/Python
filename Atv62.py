# Ler o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.
c = 1
primeiro = int(input('Qual o primeiro termo da PA ?'))
razao = int(input('Qual a razão da PA?'))

while c < 11:
    if c == 1:
        print(f'Os 10 primeiros termos da PA são: ', end='')

    print(f'{primeiro}', ',' if c < 10 else '.', end='') # não consegui tirar o espaço depois do número
    primeiro = primeiro+razao
    c += 1
