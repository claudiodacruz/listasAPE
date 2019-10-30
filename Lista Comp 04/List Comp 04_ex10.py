'''
10. Leia um vetor com 10 posições e faça a sua ordenação sem usar o comando sort()
'''

# DEFININDO OS PARÂMETROS
import random
v = []
n = 100

# GERANDO OS NÚMEROS DO VETOR DE 'n' ELEMENTOS
ni = random.randint(1,100)
v.append(ni)

while (len(v)) < n:
    num = random.randint(1,100)
    k = 1           #parâmetro de fuga
    # garantindo que o menor número seja v[0]
    if num < v[0]:
        v.insert(0,num)
    # verificando se o número está entre o antecessor e o predescessor  
    else:
        j = 0
        z = len(v)
        while j < z:
            if num < v[j]:
                if num not in v:
                    v.insert(j,num)
                    k = 0
            j += 1
    # se o número for maior que todos os do vetor ele ocupa a última posição
        if k > 0:
            if num not in v:
                v.append(num)
                
# EXIBINDO O VETOR ORDENADO
print(v)

