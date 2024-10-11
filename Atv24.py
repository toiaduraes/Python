#Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome ~SANTO~

cid = input('Qual o nome da cidade?')
lista = cid.split()
print('SANTO' in lista[0])