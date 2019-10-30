'''
5. Escreva um programa para ler 06 números (entre 1 e 6) distintos, ou seja,
não podem repetir. Exiba os números lidos.
'''

# PARÂMETROS INICIAIS
import random
v = []
n = 0

# GERANDO O VETOR COM NÚMEROS ALEATÓRIOS SEM REPETIÇÃO
num1 = random.randint(1,20)
v.append(num1)

while n != 5:
    num2 = random.randint(1,20)
    if num1 != num2:
        n += 1
        v.append(num2)
        num1 = num2
v.sort()
print(v)
