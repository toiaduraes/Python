#Contar valores negativos em uma lista de 10 valores:

valores = [int(input("Digite um valor:"))for _ in range(10)]

valores_negativos = sum(1 for valor in valores if valor <0)
print(f"Quantidade de valores negativos: {valores_negativos}")