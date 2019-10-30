'''
6. Escreva um programa que leia um vetor gabarito de 10 elementos.
Cada elemento de gabarito contém um número inteiro 1, 2, 3, 4 ou 5
correspondente as opções corretas de uma prova objetiva. Em seguida o
programa deve ler um vetor resposta, também de 10 elementos inteiros,
contendo as respostas de um aluno. O programa deve comparar os dois
vetores e escrever uo número de acertos do aluno.
'''

import random
n = 10

# GERANDO O GABARITO
letras = ['A','B','C','D','E']
gabarito = []
for i in range(n):
    x = random.randint(1,5)
    gabarito.append(letras[x-1])
print(gabarito)

# LENDO AS RESPOSTAS
resposta = []
for i in range(n):
    num = input(f'Informe a resposta da {i+1} ª questão: ').upper()
    resposta.append(num)

# CONFERINDO O GABARITO
cont = 0
for i in range(n):
    if resposta[i] == gabarito[i]:
        cont += 1

# IMPRIMINDO OS RESULTADOS
print('GABARITO = ',gabarito)
print('RESPOSTAS = ',resposta)
print('O número de respostas corretas do aluno é:', cont)

