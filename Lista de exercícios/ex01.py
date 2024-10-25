# Crie um algoritmo que receba o salário de um empregado e o percentual de aumento, calcule e mostre o
#valor do aumento e o novo salário. 

salario = float(input('Qual o salário do empregado? Em reais:'))
percentual = float(input('Qual o percentual de aumento? Em %'))

aumento = salario * (percentual/100)

print('O aumento do salário é de R${:.2f} \nO novo salário é de R${:.2f} ' .format(aumento, salario + aumento))

