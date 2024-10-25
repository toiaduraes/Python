#Faça um programa que determine se um número é múltiplo de 5.

multiplo = int(input("Digite um número inteiro:"))

if multiplo % 5 == 0: # testa o resto da divisao por 5 e verifica se é igual a 0
    print(f"{multiplo} é múltiplo de 5.")
else:
    print(f"{multiplo} não é múltiplo de 5.")