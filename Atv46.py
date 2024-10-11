#Programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício, indo de 10 até 0,
#Com uma pausa de 1 segundo entre eles.
t = 10
import time
time.sleep(1)
print('Contagem regressiva para os fogos!!!')
for c in range (11):
    print(f'{t}')
    t -= 1
    time.sleep(1)
print('Fogos estouram!!')
