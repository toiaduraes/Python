#Programa que leia as duas notas de um aluno, calcule e mostre a sua média
informacoes = 'Iremos calcular a média, digite as notas com ponto em vez de vírgula.'

print(f'{informacoes}')

nota1 = float(input('Qual a primeira nota?'))
nota2 = float(input('Qual a segunda nota?'))

media_notas = (nota1+nota2)/2

print('A Média das notas é: {}'.format(media_notas))