
valores = [int(input("Digite um valor:")) for x in range(10)]

qtd = sum(1 for valor in valores if valor >=5)

print(f"Quantidade de valores mnaiores ou iguais a 5: {qtd}")