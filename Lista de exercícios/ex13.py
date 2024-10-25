#Contar valores maiores ou iguais a 5 em uma lista de 20 valores

valores = [int(input("Digite um valor:")) for x in range(20)]

#print(valores)

qtd = sum(1 for valor in valores if valor >=5) # quantidade de valores maiores ou iguais a 5

print(f"Quantidade de valores maiores ou iguais a 5: {qtd}")

