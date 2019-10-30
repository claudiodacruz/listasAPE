'''05 - Uma matriz quadrada contendo valores inteiros é denominada quadrado mágico
quando a soma dos elementos de cada linha, a soma dos elementos de cada coluna e a
soma dos elementos das diagonais principal e secundária são todos iguais. Por exemplo,
a matriz seguinte é um quadrado mágico.
Escreva um programa que preencha uma matriz com valores fornecidos pelo usuário,
determine e mostre se a mesma é um quadrado mágico.'''

ordem = int(input('Informe a ordem da matriz quadrada: '))
m = []

# GERANDO A MATRIZ 
for i in range(ordem):
    linha = []
    for j in range(ordem):
        elemento = int(input(f'Infome o elemento a[{i+1}][{j+1}] da matriz: '))
        linha.append(elemento)
    m.append(linha)
print('\nMatriz')
for i in range(ordem):
    print(m[i])

# CRIANDO UM VETOR SOMA COM OS VALORES DAS SOMAS DAS LINHAS, COLUNAS E DIAGONAIS
s = []

# SOMANDO AS LINHAS E ARMAZENANDO NO VETOR SOMA
for i in range(ordem):
    soma = 0
    for j in range(ordem):
        soma += m[i][j]
    s.append(soma)
    
# SOMANDO AS COLUNAS E ARMAZENANDO NO VETOR SOMA
for i in range(ordem):
    soma = 0
    for j in range(ordem):
        soma += m[j][i]
    s.append(soma)

# SOMANDO AS DIAGONAIS E ARMAZENANDO NO VETOR SOMA
'''Diagonal Principal'''
soma = 0    
for i in range(ordem):
    soma += m[i][i]
s.append(soma)


'''Diagonal Secundária'''
soma = 0
for i in range(ordem):
    k = ordem - (i + 1)
    soma += m [i][k]
s.append(soma)

# EXIBINDO O VETOR SOMA
print()
print(s)

# VERIFICANDO SE A MATRIZ É UM CUBO MÁGICO E IMPRIMINDO OS RESULTADOS
cnt = 0
n = len(s) 
for i in range(n):
    if s[0] == s[i]: 
        cnt += 1
print()
'''A matriz será um cubo mágico se todos os elementos do vetor soma forem iguais'''
if n == cnt: 
    print('A matriz é um cubo mágico.')
else:
     print('A matriz não é um cubo mágico.')

