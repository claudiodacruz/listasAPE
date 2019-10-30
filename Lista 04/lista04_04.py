'''4. Faça um programa que leia um vetor V (contendo 30 elementos inteiros)
e um valor inteiro K, calcule e exiba a quantidade de ocorrências de K dentro
de V.'''

#GERANDO O VETOR ALEATÓRIO DE 30 ELEMENTOS
import random
n = 30
v = []
for i in range(n):
    v.append(random.randint(1,20))
print(v)

#BUSCANDO DETERMINADO ELEMENTO NO VETOR
k = int(input('Entre com o valor de k: '))
cont = 0
for i in range(n):
    if v[i] == k:
        cont += 1
print('Existe(m) {} ocorrência(s) do número {} no vetor.'.format(cont,k))
