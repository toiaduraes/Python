#Programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
#Se ele ainda vai se alistar ao serviço militar.
#Se é a hora de se alistar.
#Se já passou do tempo do alistamento.
#Também deverá mostrar o tempo que falta ou que passou do prazo.

idade = int(input('Qual a sua idade?'))

if idade == 18:
    print(f'É hora de se alistar!')
elif idade > 18:
    print(f'Passou do tempo de se alistar!')
    print(f'{idade-18} ano(s) de atraso.')
else:
    print(f'Ainda falta(m) {18-idade} ano(s) para o seu alistamento militar.')