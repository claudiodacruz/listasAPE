'''
8. Escreva uma função que receba como parâmetro uma string e a exiba na vertical,
ou seja, com uma letra em cada linha. Faça também um programa para testar a função.
'''

def lincol(n):
    m = []
    for i in n:
        linha = []
        for j in range(1):
            linha.append(i)
        m.append(linha)
    return m

v = (1,2,3,4)
m = lincol(v)
print(m)
    
    
