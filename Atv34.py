#Um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
#Para salários superiores a 1250, calcule um aumento de 10%
#Para inferiores ou iguais, o aumento é de 15%

salario = float(input('Qual o valor do salário?'))

if salario > 1250:
    print(f'O aumento será de: {salario*0.10} a mais.')
else:
    print(f'O aumento será de: {salario*0.15} a mais')