'''
4. Escreva um programa para ler 06 números. Calcule e exiba se os números lidos
são distintos, ou possui repetição.
'''

# DEFININDO PARÂMETROS
import random
v = []
n = 6

# GERANDO O VETOR ALEATÓRIO
for i in range(n):
    num = random.randint(1,30)
    v.append(num)
v.sort()
print(v)

# VERIFICANDO SE OS NÚMEROS SÂO DISTINTOS
cont = 0
for i in range(n):
    k = v[i]
    for j in range(n):
        if v[j] == k:
            cont += 1

# EXIBINDO OS RESULTADOS           
if cont == n:
    print('\nOs números lidos são distintos')
else:
    print('\nOs numeros lidos não são distintos')
    
    
