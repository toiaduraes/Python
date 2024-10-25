#Exibir números pares de uma sequência

numeros = input("Digite um número inteiro:").split()

for x in numeros:

    print (f"Analisando o número {x}...")

    if int(x) % 2 == 0:
        print(f"{x} é par.")
    else:
        print(f"{x} é ímpar.")