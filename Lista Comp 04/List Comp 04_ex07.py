'''
7. Foi elaborada uma prova objetiva contendo 200 (duzentas) questões para um
concurso público. Escreva um programa para ler a matrícula (valor inteiro),
a quantidade de acertos, quantidade de erros e a quantidade de questões não
respondidas de cada um dos 4000 (quatro mil) candidatos que fizeram essa
prova. Ao final, o programa deverá exibir o código de cada candidato que
acertou, no mínimo, 50% da prova, com respectiva taxa de acerto, erro e
questões não respondidas.
'''

import random
nq = 10
nc = 400
v = []
c = []
l = ['A','B','C','D','E']
le = ['A','B','C','D','E',' '] '''vetor com a possibilidade de serem geradas questões não respondidas'''

# GERANDO O GABARITO ALEATÓRIO
for i in range(nq):
    gab = random.randint(0,4)
    v.append(l[gab])
print(v)

# CALCULANDO O NÚMERO DE ACERTOS A PARTIR DE UMA LISTA DE RESPOSTAS ALEATÓRIAS
r = []
for i in range(nc):
    ac = 0
    nr = 0
    for j in range(nq):
        resp = random.randint(0,5)'''possibilita a existência de questões não respondidas'''
        resp = le[resp]
        if resp == v[j]:
            ac += 1
        if resp == ' ': '''calculando número de questões não respondidas'''
            nr += 1
    r.append(ac)
print(r)

# EXIBINDO A LISTA DE CANDIDATOS APROVADOS
for i in range(nc):
    if r[i] >= nq / 2:
        print('mat.',i + 1,' - ',r[i],'  ',nq - nr - r[i],' ',nr)
        
    
