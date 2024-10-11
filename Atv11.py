# Programa que lê a largura e a altura de uma parede em metros
# Cálcula a área e a quantidade de tinta necessária para pintá-la
# Sabendo que cada litro de tinta, pinta uma área de 2m²

largura = float(input('Qual a largura da parede?'))
altura = float(input('Qual a altura da parede?'))

area = largura*altura
qtd_de_tinta= area/2

print(f'Vc precisará de {qtd_de_tinta} litros de tinta')