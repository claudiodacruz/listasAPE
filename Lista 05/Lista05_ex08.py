'''
08 - A tabela seguinte apresenta a quantidade de vendas dos fabricantes de
veículos durante o período de 2011 a 2016, em múltiplos de mil unidades.
Escreva um programa que:
a) leia os dados da tabela e os armazene;
b) determine e mostre o fabricante com maiores vendas em cada ano;
c) determine e mostre o ano onde houve o maior volume de vendas;
d) determine e mostre a média de vendas de cada fabricante no período
apresentado na tabela.
'''

m =[]
lin = 4
col = 6

# GERANDO A MATRIZ PRINCIPAL
for i in range(lin):
    total =0
    linha = []
    for j in range(col):
        vendas = int(input(f'Informe o número de vendas do fabricante {i+1} no ano de {2012 + j}: '))
        linha.append(vendas)
        total += vendas
        media = round((total / col),2)
    linha.append(media)
    m.append(linha)
    
# GERANDO O VETOR SOMA ANUAL
va = []
for i in range(col):
    linha = []
    soma = 0
    ano = 2012+i
    linha.append(ano)
    for j in range(lin):
        soma += m[j][i]
    linha.append(soma)
    va.append(linha)

#IMPRIMINDO AS MATRIZES    
print('\nMatriz')
for i in range(lin):
    print(m[i])
print('\nVendas por ano')
for i in range(col):
    print(va[i])
print('\n')

#VERIFICANDO O FABRICANTE COM MAIOR VOLUME DE VENDAS
for j in range(col):
    fab = 0
    maior= 0
    for i in range(lin):
        if m[i][j] > maior:
            maior = m[i][j]
            fab = i + 1
    print(f'Em {2012+j}, o vendedor com maior volume de vendas foi',fab)

#VERIFICANDO O ANO COM MAIOR VOLUME DE VENDAS
maior = 0
for i in range(col):
    if va[i][1] > maior:
            maior = va[i][1]
            mano = va[i][0]
print('\nO ano com maior número de vendas foi:',mano)
print('\n')

#EXIBINDO A MÉDIA DE VENDAS POR FABRICANTE
med = []
for i in range(lin):
    linha = []
    linha.append(i + 1)
    linha.append(m[i][6])
    med.append(linha)
for i in range(lin):
    print(med[i])

