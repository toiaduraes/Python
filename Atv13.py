#Um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

salario = float(input('Qual o valor do salário que deseja aumentar em 15%?'))

print(f'O valor do salário com aumento é: {(salario*0.15)+salario}')
#nao é necessario criar uma nova variável, apenas se a intenção for usar o valor lá na frente.