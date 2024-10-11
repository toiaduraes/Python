# melhorar o programa anterior.
# Perguntar ao usuário se ele deseja mostrar mais alguns termos. Caso não, o programa encerra quando ele disser
# que quer mostrar 0 termos.

c = 1
primeiro = int(input('Qual o primeiro termo da PA ?'))
razao = int(input('Qual a razão da PA?'))

while c < 11:
    if c == 1:
        print(f'Os 10 primeiros termos da PA são: ', end='')

    print(primeiro, ',' if c < 10 else '.', end='') # não consegui tirar o espaço depois do número
    primeiro +=razao
    c += 1
    if c == 11:
        teste = int(input('\nDigite quantos termos deseja ver a mais da PA:'))
        b = 1
        d = teste
        if teste == 0:
            print('Finalizando programa!')
        while teste != 0:
            if b == 1:
                print (f'A continuação é:', end='') # parei aqui, quero que esse print apareça apenas uma vez
                b += 1
            print(primeiro,',' if teste != 1 else '.', end = '')
            primeiro = primeiro + razao
            teste -= 1
            if teste == 0:
                teste = int(input('\nDigite quantos termos deseja ver a mais da PA:'))

print('\nFinalizando programa!')