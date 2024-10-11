#Crie um programa que leia dois valores e mostre um menu na tela:
#[1] somar
#[2] multiplicar
#[3] maior
#[4] novos números
#[5] sair do programa
#Seu programa deverá realizar a operação solicitada em cada caso.
import time
print('====== Bem-Vindo ao Menu! =======')
num1 = float(input('Digite um número:'))
num2 = float(input('Digite outro número:'))

menu = 0
while menu != 5:
    print('****** Digite o número correspondente *****')
    menu = int(input(f'=======================\n'
                     f'[1] somar\n'
                     f'[2] multiplicar\n'
                     f'[3] maior\n'
                     f'[4] novos números\n'
                     f'[5] sair do programa\n'
                     f'=======================\n'
                     f': '))
    if menu == 1:
        print(f'A soma dos números é: {num1+num2}')
        time.sleep(2)
    elif menu == 2:
        print(f'A multiplicação dos números é: {num1*num2}')
        time.sleep(2)
    elif menu == 3:
        lista = [num1,num2]
        print(f'O maior número é: {max(lista)}')
        time.sleep(2)
    if menu == 4:
        num1 = float(input('Digite um número:'))
        num2 = float(input('Digite outro número:'))

print('Fim do programa!')