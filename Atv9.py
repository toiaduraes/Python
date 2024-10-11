#Programa que lê um inteiro e mostra sua tabuada usando while

num = int(input('Qual o número deseja saber a tabuada?'))
count = 1
tabuada = num
while count < 11:
    print (f'Número para a tabuada de {num} é: {num*count}')
    count = count + 1