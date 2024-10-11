#Programa que faça o computador "pensar" em um número inteiro entre 0 e 5
#E peça para o usuário tentar descobrir qual foi o número escolhido pelo pc.
#O programa deverá escrever na tela se o usuário venceu ou perdeu.
import random

lista = [0,1,2,3,4,5]
random.shuffle(lista) #random=aleatório e shuffle=embaralhar

print('Vamos brincar! :) O jogo é de adivinhação!')
print('Acabei de pensar em um número, se você acertar qual foi... Vc ganha!')
num_adv = int(input('Entre 0 e 5, qual número você acha que eu escolhi?'))

if lista[3] == num_adv:
    print('Você acertou!')

else:
    print('Você errou :( e eu ganhei !!!')
    print (f'O número escolhido por mim foi: {lista[3]}')
print('===!fim!===' * 3)