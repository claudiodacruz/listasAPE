'''
2. Faça um programa que leia um vetor V(contendo 20 elementos inteiros) e
um valor inteiro K, verifique e exiba se o elemento está ou não no vetor.
Se estiver informe em que posição.
Obs: o numero pode se repetir no vetor, nesse caso, mostre as posições.
'''

import random

# INCIANDO OS PARÂMETROS
v = []
ind = []
n = 20

# GERANDO O VETOR
for i in range(n):
    num = random.randint(0,20)
    v.append(num)
print(v)

# VERIFICANDO O ELEMENTO
k = int(input('Informe um número inteiro: '))
for i in range(n):
    if k == v[i]:
        ind.append(i)
print('A posição do número {} é {}'.format(k,ind))

