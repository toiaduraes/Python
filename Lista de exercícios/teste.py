largura = 60
altura = 10

for linha in range(altura):
    if linha == 0 or linha == altura - 1:
        print("+" * largura)
    else:
        print("+" + " " * (largura - 2) + "+")