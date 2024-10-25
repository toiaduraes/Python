#Ler a hora de início e a hora de fim de um jogo de Xadrez (considere apenas horas inteiras, sem os minutos)
#e calcule a duração do jogo em horas, sabendo-se que o tempo máximo de duração do jogo é de 24 horas e que
#o jogo pode iniciar em um dia e terminar no dia seguinte.

inicio = int(input("Digite a hora de início do jogo:"))
fim = int(input("Digite a hora do fim do jogo:"))

if fim > inicio:
    durancao = fim - inicio
else: 
    duracao = 24 - inicio + fim

