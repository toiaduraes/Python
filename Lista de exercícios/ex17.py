#Somar números positivos em uma lista de 10 valores

valores = [int(input("Digite um valor:")) for _ in range(10)]

soma = sum(valor for valor in valores if valor >0)
print(f"A soma dos valores positivos é: {soma}")