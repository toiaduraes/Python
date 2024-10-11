altura = int(input('qual a altura do banheiro ?'))
largura_maior = int(input('Qual a largura da maior parede?'))
largura_menor = int(input('Qual a largura da menor parede?'))
#portas = int(input('Quantas portas terá o ambiente? '))
#janelas = int(input('Quantas janelas terá o ambiente?'))
#nicho = input('Qual o tamanho do nicho?')
#pia= input('Qual o tamanho da pia?')
#vaso = int(input('Quantos vasos?'))
#espelho = input('Qual o tamanho do espelho?')
#torneira = input ('Quantas torneiras?')

q1 = altura*largura_maior #Quadrado
r1 = altura*largura_menor #Retângulo
chao = largura_maior*largura_menor

n1 = (r1+chao)#detalhe do fundo da parede + o chão
n2 = ((q1*2)+r1)#parede do espelho + parede oposta ao espelho + parede da porta sem a porta
#porta =int()

#print('A sua lista de compras será: {} m² do porcelanato cinza, {} m² do porcelanato branco'.format(n1,n2))
#print('{} porta(s), {} janela(s), {} nicho, {} pia, {} vaso, {} espelho, {} torneira'.format(portas,janelas,nicho,pia,vaso,espelho,torneira))

valor_n1 = float(input('Qual o valor do porcelanato cinza?'))
valor_n2 = float(input('Qual o valor do porcelanato branco?'))
valor_argamassa = float(input('Qual o valor da Argamassa?'))
valor_rejunte = float(input('Qual o valor do rejunte?'))
#valor_espelho = float(input('Qual o valor do m² do espelho?'))

total = (n1*valor_n1)+(n2*valor_n2)+(((n1+n2)/3)*valor_argamassa)+(((n1+n2)/3)*valor_rejunte)

print('O valor da lista de compras (Porcelanato,Argamassa e rejunte) é: {}'.format(total))
