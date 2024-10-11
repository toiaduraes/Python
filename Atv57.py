#Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores M ou F. Caso esteja errado, peça
# a digitação novamente até ter um valor correto.

sexo = str(input('Qual o sexo da pessoa?')).strip().upper()[0]

while sexo != 'M' and sexo != 'F':
#while sexo not in ‘MnFf’ - ou seja, se a variável não conter nenhuma dessas, o laço continua.-

    print ('O valor digitado está incorreto, pressione F para Feminino ou M para Masculino.')
    sexo = str(input('Qual o sexo da pessoa?'))
