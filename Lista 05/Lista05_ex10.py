'''
10. A distância entre várias cidades é dada pela tabela abaixo (em km):
Faça um programa que:
a) armazene estas informações;
b) mostre a distância percorrida para um determinado percurso.
Ex: dado o percurso 1, 2, 3, 2, 5, 1, 4, a distância percorrida
é 15+10+10+28+12+5 = 80km.
'''
import random
m = []
n = 5
linha = [0]

#GERANDO UMA MATRIZ SIMÉTRICA
for c in range(n):
    linha.append(c + 1)
m.append(linha)
for i in range(n):
        linha = []
        linha.append(i + 1)
        for j in range(n):
            linha.append(0)
        m.append(linha)
for i in range(1,n):
    for j in range(0,i):
        m[i][j] = random.randint(1,100)
        m[j][i] = m[i][j]

#EXIBINDO A MATRIZ DE DISTANCIAS
for i in range (n):
    for j in range(n):
        print('{0:4d}'.format(m[i][j]),end='')
    print()
    

#CALCULANDO O PERCURSO DESEJADO
dist = 0
q = 'N'
cid1 = int(input('Informe as cidades do percurso: '))
while q == 'N':
    cid2 = int(input('Informe as cidades do percurso: '))
    q = input('O percurso foi finalizado (S) ou (N)? ')
    q = q.upper()
    dist += m[cid1-1][cid2-1]
    cid1 = cid2
print(f'A distância percorrida será de {dist} Km.')
    

    
