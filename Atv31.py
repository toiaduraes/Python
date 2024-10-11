#P. que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$ 0,50 por Km para viagens
#De até 200km e R$ 0,45 para viagens mais longas.

distancia = float (input('Qual é a distância da sua viagem?'))

if distancia <= 200:
    print(f'O valor da sua passagem será de R$ {distancia*0.50} Reais.')
else:
    print(f'O valor da sua passagem será de R$ {distancia*0.45} Reais.')