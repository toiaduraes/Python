#Programa que lê um valor em metros e exibe sua conversão em cm e mm

valor = float(input('Qual o valor em Metros deseja converter para Cm e Mm?'))

cm = valor*100
mm = valor*1000

print(f'O valor em cm é:{cm} \nO valor em mm é: {mm}')