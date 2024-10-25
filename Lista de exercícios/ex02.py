#Escreva uma algoritmo que receba uma hora no formato de três números inteiros que representam: horas,
#minutos e segundos. Sua função deve calcular e retornar a #quantidade total de segundos.

print('Você irá digitar três números inteiros para representar as horas, minutos e segundos.')

horas = int(input('Digite a hora:'))
minuto = int(input('Digite os minutos:'))
segundos = int(input('Digite os segundos'))

total_segundos = (horas * 3600) + (minuto * 60) + segundos

print('O total de segundos é de:', total_segundos)