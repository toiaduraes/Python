#programa para aprovar o empréstimo bancário para a compra de uma casa.
# O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
#Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o emprétimo
#será negado.

val_casa = float(input('Qual o valor da casa?'))
val_sal = float(input('Qual o seu salário?'))
tempo = float(input('Em quanto tempo irá pagar?'))
prestacao = (val_casa/tempo)



if prestacao <= (0.30*val_sal):
    print(f'Seu empréstimo foi aprovado e a prestação da sua casa será de: {prestacao}'
    )
else:
    print(f'Seu empréstimo foi recusado pois a prestação excede 30% o valor do seu salário.\n'
        f'O valor máximo para a prestação, de acordo com seu salário, seria de: {0.30*val_sal}Reais \n'
          f'A Prestação desta casa é de: {prestacao:.2f}') #limitado a duas casas decimais depois da vírgula