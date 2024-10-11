#20:00
#Programa que leia uma frase pelo teclado e mostre:
#Quantas vezes aparece a letra "A"
#Em que posição ela aparece a primeira vez
#Em que posição ela aparece a última vez

frase = str(input('Qual a frase deseja testar?'))

print(f'A letra A aparece {frase.count('A')} vezes.\n'
      f'Ela aparece a primeira vez na posição: {frase.find('A')}\n'
      f'Ela aparece a última vez na posição: {frase.rfind('A')} ')