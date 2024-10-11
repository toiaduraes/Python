#Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada

num = int(input('Qual o número vc quer saber o dobro, triplo e raiz quadrada?'))

dobro = num*2
triplo =num*3
raiz = num**(1/2)

print('Número: {}\nDobro: {}\nTriplo: {}\nRaiz quadrada:{}'.format(num,dobro,triplo,raiz))