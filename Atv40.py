#Programa que leia duas notas de um aluno e calcule a sua média.
#Média abaixo de 5.0: REPROVADO
#Média entre 5.0 e 6.9: RECUPERAÇÃO
#Média 7.0 ou superior: APROVADO

nota1 = float(input('Qual a primeira nota do aluno?'))
nota2 = float(input('Qual a segunda nota do aluno?'))

if (nota1+nota2)/2 < 5:
    print(f'REPROVADO(A)')
elif 5 <= (nota1+nota2)/2 <= 6.9:
    print(f'RECUPERAÇÃO')
else:
    print(f'APROVADO')

