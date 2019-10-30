'''
Escreva um programa que leia a idade de um nadador e classifique-o em uma
das seguintes categorias:
a) infantil A = 5 a 7 anos
b) infantil B = 8 a 10 anos
c) juvenil A = 11 a 13 anos
d) juvenil B = 14 a 17 anos
e) adulto = maiores de 18 anos
'''
idade = int(input('Qual a idade do nadador: '))
if idade <= 4:
    cat = '"sem categoria"'
elif idade > 17:
    cat = '"adulto"'
elif idade > 13:
    cat = '"juvenil B"'
elif idade > 10:
    cat = '"juvenil A"'
elif idade > 7:
    cat = '"infantil B"'
else:
    cat = '"infantil A"'
print('A categoria é {}.'.format(cat))
              
