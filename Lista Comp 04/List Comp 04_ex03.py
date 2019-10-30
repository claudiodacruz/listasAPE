'''
3. Escreva um programa para ler 20(vinte) números. Calcule e exiba quantos
desses números possuem valor abaixo da média dos números lidos.
'''

# INICIANDO AS VARIÁVEIS
import random
n = 20
v = []
soma = 0

# GERANDO O VETOR E CALCULANDO A MÉDIA
for i in range(n):
    num = random.randint(1,100)
    v.append(num)
    soma += num
media = soma / n
print(v)
print(media)

# CALCULANDO OS NÚMEROS ABAIXO DA MÉDIA
mi = []
for i in range(n):
    if v[i] < media:
        mi.append(v[i])
tam = len(mi)
print(mi)
print(tam)
        
