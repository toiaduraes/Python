#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a
#quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar,
# sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

km_percorridos = float(input('Quantos km foram percorridos?'))
dias_alugados = float(input('Por quantos dias permaneceu alugado?'))

print(f'O valor a ser pago pelo carro é de R${(dias_alugados*60)+(km_percorridos*0.15)} reais')