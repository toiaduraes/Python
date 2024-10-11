#A confederação nacional de natação precisa de um programa que leia o
#Ano de nascimento de um atleta e mostre sua categoria, de acordo com a sua
#idade:

#até 9 anos: mirim
#até 14 anos: infantil
#até 19 anos: junior
#até 20 anos: sênior
#acima: MASTER

ano = int(input('Em que ano o atleta nasceu?'))

if 2024-ano <= 9:
    print('Mirim')
elif 9 < 2024-ano <= 14:
    print('Infantil')
elif 14 < 2024-ano <= 19:
    print('Junior')
elif 19 < 2024-ano <= 20:
    print ('Sênior')
else:
    print('MASTER')