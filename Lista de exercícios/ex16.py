#Calcular a média de 10 valores

valores = [float(input("Digite o valor: ")) for _ in range (10)]
media = sum(valores)/len(valores)
print(f"Media dos valores é: {media}")