'''
7. Dada a matriz M, escreva um programa que gere uma matriz N, cujos elementos
são os elementos de M com os valores das suas bordas substituídos por 0 (zero).
Crie uma função borda que receba uma matriz e substitua os elementos de suas
bordas por 0 (zero).
M = 6, 2, 8, 1, 5       N = 0, 0, 0, 0, 0
    3, 7, 5, 2, 1           0, 7, 5, 2, 0
    4, 8, 1, 3, 2           0, 8, 1, 3, 0
    8, 6, 4, 2, 7           0, 0, 0, 0, 0
'''

def transf(m):
    n = []
    
    for i in range(4):
        linha = []
        for j in range(5):
            k = m[i][j]
            if i == 0 or i == 3 or j ==0 or j == 4:
                linha.append(0)
            else:
                linha.append(k) 
        n.append(linha)
    return n
    
m = [(6, 2, 8, 1, 5),(3, 7, 5, 2, 1),(4, 8, 1, 3, 2),(8, 6, 4, 2, 7)]
n = transf (m)
print(n)

