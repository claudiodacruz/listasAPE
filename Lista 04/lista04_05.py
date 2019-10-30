'''Faça um programa que leia um vetor de 10 números inteiros e gere um segundo
vetor (que deve ser impresso), cujas posições pares são o dobro do  vetor original
e as ímpares o triplo'''

#GERANDO O VETOR ALEATÓRIO
import random
v = []
for i in range(10):
    num = random.randint(1,10)
    v.append(num)
print(v)

#GERANDO O VETOR COM ALTERAÇÕES
w = []
for i in range(10):
    if i % 2 == 0:
        w.append(v[i] * 2)
    else:
        w.append(v[i] * 3)
print(w)


        
        
    
