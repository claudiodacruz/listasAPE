'''02 - Escreva um programa que, dada uma matriz quadrada de ordem N,
de elementos inteiros, exiba os elementos da diagonal principal, isto é,
os elementos onde I = J.
Obs: N será lido (N <= 10).'''

import random

ordem = int(input('Informe a ordem da matriz: '))
m = []
d = []

# GERANDO A MATRIZ 
for i in range(ordem):
    linha = []
    for j in range(ordem):
        elemento = random.randint(0,9)
        linha.append(elemento)
        # CRIANDO O VETOR DA DIAGONAL
        if i == j:
            d.append(elemento)
    m.append(linha)

# IMPRIMINDO OS RESULTADOS
for i in range(ordem):
    print(m[i])
print('\nOs elementos da diagonal principal são: ',d)

        
