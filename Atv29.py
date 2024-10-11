#Escreva um programa que leia a velocidade de um carro.
#Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado.
#A multa vai custar R$7,00 por cada Km acima do limite.

v = float(input('Qual a velocidade do carro?'))

if v >= 80:
    print(f'O carro ultrapassou a velocidade máxima e será multado em R${(v-80)*7} reais')
else:
    print('O carro está na velocidade permitida que é de até 80km/h.')
