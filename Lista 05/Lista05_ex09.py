'''
09 - Uma análise dos acidentes de trânsito está sendo realizada em Manhattan, New York. 
As ruas 30 a 38 e as avenidas primeira a décima foram estudadas. Os elementos da matriz 
(avenida X rua) indicam o número de acidentes ocorridos nas proximidades, no período estudado. 
Um número desconhecido de dados de acidentes é lido. Faça um programa para, a partir da informação 
acima, gerar a matriz de acidentes entre determinadas avenidas e ruas de New York.  
'''

# DEFININDO OS PARÂMETROS
m = []
linha = [' ']
lin = 10
col = 9

for j in range(col):
    par = 30 + j
    linha.append(par) 
m.append(linha)

# GERANDO UMA MATRIZ NULA
for i in range(lin):
        linha = []
        linha.append(i + 1)
        for j in range(col):
            linha.append(00)
        m.append(linha)

# INFORMANDO OS ACIDENTES
reg = input('Deseja informar algum acidente (S) ou (N)? ').upper()
while reg == 'S':
    av = int(input('Informe o número da avenida: '))
    rua = int(input('Informe o número da rua: '))
    rua = rua - 29
    m[av][rua] += 1
    reg = input('Deseja informar algum acidente (S) ou (N)? ').upper()

# EXIBINDO OS RESULTADOS
print('\n')
for i in range(col+1):
    print(m[0][i],end='  ')
trac = '-'*4*(col)
print('\n',trac)
for i in range(1,col+1):
    for j in range(lin):
        print(m[i][j],end='   ')
    print()
