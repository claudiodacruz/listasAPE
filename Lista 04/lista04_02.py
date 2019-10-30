''' 2 - Faça um programa que leia um vetor de N números inteiros (N <= 100),
inverta a ordem dos elementos do vetor e exiba o vetor invertido.
Obs: É necessário inverter os elementos do vetor, não basta imprimi-los em ordem inversa!
'''

import random
n = int(input('Inmforme o número de elementos do vetor.'))
v = []
r = []

for i in range (n):
    num = random.randint(1,100)
    v.append(num)
print(v)
for i in range (n,0,-1):
    inv = v[i-1]
    r.append(inv)
print(r)  


