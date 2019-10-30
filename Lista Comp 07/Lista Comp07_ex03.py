'''
3. Dado o vetor X = { 8,9,3,5,7,2,6,4,8 }, escreva programa que gere um vetor Y
cujos elementos são os elementos de X com os números pares substituídos por 99.
Crie uma função par que receba um vetor e substitua seus números pares por 99.
'''

'''
def par(v):
    v2 = []
    n = len(v)
    for i in range(n):
        if v[i] % 2 == 0:
            v[i] = 99
'''

def par(v):
    n = len(v)
    for i in range(n):
        if v[i] % 2 == 0:
            v[i] = 99

x = [8,9,3,5,7,2,6,4,8]
y = x[:]
par(y)
print('x = ',x)
print('y = ',y)
