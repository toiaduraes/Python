#Crie um programa que leia o nome de uma pessoa e mostre:
#O nome com todas as letras MAIÚSCULAS
#O nome com todas as letras MINÚSCULAS
#Quantas letras ao todo (sem considerar os espaços)
#Quantas letras tem o primeiro nome

nome = str(input('Qual o nome da pessoa?'))

nome_sem_espaco= nome.split()
print('1- Fatiou a string e criou uma lista:', nome_sem_espaco)
primeiro_n = nome_sem_espaco[0]
print('2- Primeiro nome da lista fatiada anteriormente: ',primeiro_n)
comprimento = len(nome)
print('3- Comprimento da string completa digitada (letras+espaço): ',comprimento)
comprimento_espaços = nome.count(' ')
print('4- Quantidade de espaços que a string digitada contém: ',comprimento_espaços)

print(f'Maíusculas: {nome.upper()},Minúsculas: {nome.lower()},Qtd de letras sem espaços: {comprimento-comprimento_espaços},'
        f' Qtd de letras do primeiro nome:{len(primeiro_n)} ')