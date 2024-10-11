#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

produto = float(input('Qual o valor do produto que deseja ter 5% de desconto?'))

desconto = produto*0.05
produto = produto - desconto
print(f'O novo valor com desconto é: {produto}')