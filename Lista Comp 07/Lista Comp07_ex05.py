'''
5. Escreva um programa que leia 100 números inteiros e armazene no vetor L. Leia
um número N e informe se ele está no vetor L. Crie uma função acha que retorna
True se um determinado número pertence a um vetor e False, caso contrário.
'''

def proc(n,k):
    a = 0
    for i in k:
        if i == n:
            a += 1
    if a > 0:
        return True
    else:
        return False
        
import random
l = []
for i in range(100):
    l.append(random.randint(0,100))


n = int(input("Informe um número inteiro de 0 a 100: "))
valor = proc(n,l)
l.sort()
print(l)
print(valor)
        
