'''
6. Faça um programa que leia duas matrizes de inteiros e gere uma terceira
matriz que corresponderá a soma das duas matrizes lidas. A ordem das matrizes
também será lida. O programa deverá conter as seguintes funções:
a) Uma função para ler uma matriz, sendo passados como parâmetros a ordem da
matriz;
b) Uma função para exibir uma matriz em sua representação clássica (linhas e
colunas).
c) Uma função para somar duas matrizes.
'''

#FUNÇÃO PARA LER A MATRIZ
def lerMatriz(nl,nc):
    m=[]
    for i in range (nl):
        linha = []
        for j in range(nc):
            n = int(input('Elemento '+str(i)+','+str(j)+': '))
            linha.append(n)
        m.append(linha)
    return m

#FUNÇÃO PARA EXIBIR A MATRIZ
def exibirMatriz(m):
    nl = len(m)
    nc = len(m[0])
    for i in range (nl):
        for j in range(nc):
            print(m[i][j],' ',sep='',end='')
        print()
    return

#FUNÇÃO PARA SOMAR AS MATRIZES
def somaMatriz(a,b):
    c = []
    nl = len(a)
    nc = len(a[0])
    for i in range(nl):
        linha = []
        for j in range(nc):
            n = a[i][j] + b[i][j]
            linha.append(n)
        c.append(linha)
    return c

#PROGRAMA PARA SOMAR MATRIZ
lin = int(input('Informe o número de linhas: '))
col = int(input('Informe o número de colunas: '))
print("Informe os elementos da 1ª matriz")
matrizA = lerMatriz(lin,col)
print("Informe os elementos da 2ª matriz")
matrizB = lerMatriz(lin,col)
matrizC = somaMatriz(matrizA,matrizB)


        
    
