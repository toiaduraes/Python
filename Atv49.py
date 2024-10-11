#Tabuada do número que o usuário escolher.

num = int(input('Qual o número deseja saber a tabuada?'))

for c in range (11):
    print (f'{c} x {num} = {c*num}')