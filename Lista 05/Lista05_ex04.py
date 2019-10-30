'''04 - Uma matriz de permutação é uma matriz quadrada cujos elementos são 0's
ou 1's, tal que em cada linha e em cada coluna exista apenas um elemento igual
a 1. Por exemplo, a matriz seguinte é uma matriz de permutação.
Com base na definição apresentada, escreva um programa que preencha uma matriz
quadrada com valores fornecidos pelo usuário, determine e mostre se a mesma é
uma matriz de permutação.'''

import random
ordem = int(input('Informe a ordem da matriz: '))
m = []

# GERANDO A MATRIZ
for i in range(ordem):
    linha = []
    for j in range(ordem):
        elemento = int(input(f'Informe o elemento a[{i+1}][{j+1}] da matriz: '))
        linha.append(elemento)
    m.append(linha)
print()
for i in range(ordem):
    print(m[i])
print()

# TESTANDO AS LINHAS
testel = 0
for i in range(ordem):
    cont1 = 0
    for j in range(ordem):
        if m[i][j] == 1:
            cont1 += 1
    
    if cont1 > 1 or cont1 == 0:
        testel += 1

# TESTANDO AS COLUNAS
testec = 0
for i in range(ordem):
    cont1 = 0
    for j in range(ordem):
        if m[j][i] == 1:
            cont1 += 1
    
    if cont1 > 1 or cont1 == 0:
        testec += 1

# IMPRIMINDO OS RESULTADOS
if testel > 1 or testec > 1:
    print('Não é uma matriz permutação')
else:
    print('É uma matriz permutação')
