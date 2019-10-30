'''06 - Escreva um programa que preencha uma matriz 3x3 com valores inteiros
fornecidos pelo usuário. O programa deverá calcular e exibir:
a) A soma dos elementos de cada linha;
b) A soma dos elementos de cada coluna;
c) A soma dos elementos da diagonal principal da matriz;
d) A soma dos elementos da diagonal secundária da matriz;
e) A soma de todos os elementos da matriz.'''

ordem = 3
m = []

for i in range(ordem):
    linha = []
    for j in range(ordem):
        elemento = int(input(f'Infome o elemento a[{i+1}][{j+1}] da matriz: '))
        linha.append(elemento)
    m.append(linha)
print('\nMatriz')
for i in range(ordem):
    print(m[i])

s = []

#SOMANDO AS LINHAS
for i in range(ordem):
    soma = 0
    for j in range(ordem):
        soma += m[i][j]
    s.append(soma)
    
#SOMANDO AS COLUNAS
for i in range(ordem):
    soma = 0
    for j in range(ordem):
        soma += m[j][i]
    s.append(soma)

#SOMANDO AS DIAGONAIS

'''Diagonal Principal'''
soma = 0    
for i in range(ordem):
    soma += m[i][i]
s.append(soma)

'''Diagonal Secundária'''
soma = 0
for i in range(ordem):
    k = ordem - (i + 1)
    soma += m[i][k]
s.append(soma)

#SOMANDO TODOS OS ELEMENTOS
soma = 0
for i in range(ordem):
    soma += s[i]

# IMPRIMINDO O VETOR SOMA
print('\nVetor Soma')
print(s)

# IMPRIMINDO OS RESULTADOS
print()
n = 2 * ordem
for i in range(ordem):
    print('A soma da',i+1,'ª linha é: ',s[i])
for i in range(ordem,n):
    print('A soma da',i+1,'ª coluna é: ',s[i])
for i in range(2):
    print('A soma da',i+1,'ª diagonal é: ', s[i+n])
print('A soma de todos os elementos da matriz é: ',soma)

