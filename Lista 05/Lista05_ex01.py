''' 01 - Escreva um programa que preencha duas matrizes 2x3 com valores inteiros
fornecidos pelo usuário. O programa deverá somar as duas matrizes,
armazenando o resultado em uma terceira matriz, que deverá ser exibida.'''


lin = 2
col = 3

# INFORMANDO A 1ª MATRIZ
print('Informe os elementos da 1º matriz')
print()
a = []
for i in range(lin):
    linha = []
    for j in range(col):
        elem = int(input(f'Informe o valor da {1+i}ª linha e da {1+j}ª coluna: '))
        linha.append(elem)
    a.append(linha) 


# INFORMANDO A 2ª MATRIZ
print('\nInforme os elementos da 1º matriz')
print()
b= []
for i in range(lin):
    linha = []
    for j in range(col):
        elem = int(input(f'Informe o valor da {1+i}ª linha e da {1+j}ª coluna: '))
        linha.append(elem)
    b.append(linha) 


# GERANDO A MATRIZ SOMA
c =[]
for i in range(lin):
    linha = []
    for j in range(col):
        soma = a[i][j] + b[i][j]
        linha.append(soma)
    c.append(linha)

# IMPRIMINDO AS MATRIZES
print()
for i in range(lin):
    print(a[i])
print()
for i in range(lin):
    print(b[i])
print()   
for i in range(lin):
    print(c[i])

