'''03 - Uma matriz transposta é a matriz que se obtém da troca de linhas
por colunas de uma dada matriz. Assim, dada uma matriz C de ordem m x n,
a matriz transposta dela será representada por Ct de ordem n x m onde cada
elemento de Ct [i,j] = C [j,i].
Escreva um programa que preencha uma matriz 4x3 com valores reais fornecidos
pelo usuário e mostre a sua transposta. Dada uma matriz A de ordem m x n,
a matriz transposta dela será representada por At de ordem “invertida” n x m.'''

import random
a = []
t = []
lin = 4
col = 3

# GERANDO A MATRIZ
for i in range(lin):
    linha = []
    for j in range (col):
        elemento = random.randint(0,9)
        linha.append(elemento)
    a.append(linha)

# GERANDO A MATRIZ TRANSPOSTA
for i in range(col):
    linha = []
    for j in range(lin):
        elemento = a[j][i]
        linha.append(elemento)
    t.append(linha)

# IMPRIMINDO OS RESULTADOS
for i in range(lin):
    print(a[i])
print()
for i in range(col):
    print(t[i])
