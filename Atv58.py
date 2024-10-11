# Melhore o jogo do desafio 028 onde o computador vai "pensar" em um número entre 0 e 10.
# Só que agora o jogador vai tentar adivinhar até acertar,
# mostrando no final quantos palpites foram necessário para vencer.

from random import randint
pc = randint(0, 11)  # o pc irá sortear um num entre o intervalo indicado

num_usu = int(input('Qual o número vc acha que eu pensei?'))
while pc != num_usu:
    num_usu = int(input(' Você errou HAHAH. Tente novamente. Qual o número vc acha que eu pensei?'))
print(f'Parabéns, o número que eu pensei realmente foi esse! {pc}')




