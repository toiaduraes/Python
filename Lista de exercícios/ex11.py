#Calcular a soma das idades do homem mais velho com a mulher mais nova e o produto das idades do homem mais novo com a mulher mais velha:

homem1 = int(input("Digite a idade do primeiro homem:"))
homem2 = int(input("Digite a idade do segundo homem:"))
mulher1 = int(input("Digite a idade da primeira mulher:"))
mulher2 = int(input("Digite a idade da segunda mulher:"))

homem_velho = max(homem1, homem2)
homem_novo = min(homem1, homem2)
mulher_velha = max(mulher1, mulher2)
mulher_nova = min(mulher1, mulher2)

soma = homem_velho + mulher_nova
produto = homem_novo * mulher_velha

print(f"A soma das idades do homem mais velho e da mulher mais nova é {soma}")
print(f"O produto das idades do homem mais novo com a mulher mais velha é {produto}")
