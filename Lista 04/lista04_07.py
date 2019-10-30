'''
7. Utilize vetores para representar operações sobre conjuntos. Faça um programa para:
a) gerar um vetor A com valores randômicos (entre 0 e 99). O tamanho de A também será
randômico. Não deve haver valores repetidos no vetor.
b) gerar um vetor B da mesma maneira.
c) gerar um novo vetor D que corresponde à união dos vetores A e B.
d) imprimir os vetores A, B, C e D.
'''

import random
# GERANDO O CONJUNTO A 
a = []
tamA = random.randint(1,10)
print(tamA)
while len(a) != tamA:
    r = (random.randint(0,9))
    if r not in a:
        a.append(r)
a.sort()
print(a)

# GERANDO O CONJUNTO B
b = []
tamB = random.randint(1,10)
print(tamB)
while len(b) != tamB:
    s = (random.randint(0,9))
    if s not in b:
        b.append(s)
b.sort()
print(b)

# FAZENDO A INTERSECÇÃO
c = []
for i in range(tamA):
    if b.count(a[i]) > 0:
        c.append(a[i])
print(c)

# FAZENDO A UNIÃO
d = []
for i in range (tamA):
    d.append(a[i])
for i in range(tamB):
    if b[i] not in d:
        d.append(b[i])
'''
outra forma

for i in range(tam(tamB):
    if d.count(b[i]) == 0:
        d.append(b[i])
'''
d.sort()
print(d)

