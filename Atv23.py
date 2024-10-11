#Programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados

num = str(input('Qual o número deseja saber a unidade, dezena, centena e milhar?'))
print(f'Unidade: {num[3]} '
      f'Dezena: {num[2]} '
      f'Centena: {num[1]} '
      f'Milhar: {num[0]}')