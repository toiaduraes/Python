#Lê o nome completo de uma pessoa, mostrando em seguida,
# o primeiro e o último nome separadamente.

nome = str(input('Digite o nome completo:'))
frase = nome.split()

print(f'O primeiro nome é: {frase[0]}.'
      f'O último nome é: {frase[-1]}.')