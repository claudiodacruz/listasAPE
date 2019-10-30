'''
08 - Faça um programa para ler 8 dezenas apostadas por 60 apostadores e
verificar se a aposta é válida(cada dezena está entre [1, 80] e não pode
haver repetição). Sendo válida, o programa deverá calcular e exibir a
quantidade de números acertados em cada aposta. Não sendo válida, o programa
deverá exibir “aposta inválida”.
Atenção! Dezenas sorteadas são: 06, 07, 13, 14 e 26.
'''

import random
s = [6,7,13,14,26]
v = []
n = 8
a = 10
print(s)

for k in range(a):
    ac = 0
    v = []
# GERANDO UMA APOSTA ALEATÓRIA
    num = random.randint(1,80)
    v.append(num)
    par = 0
    while len(v) < n:
        if num not in v:
            v.append(num)
        num = random.randint(1,85)# possibilidade de gerar uma aposta inválida
        if num > 80:
            par = ' aposta inválida'
    v.sort()
    print('\n',v)


# FAZENDO A CONFERÊNCIA DAS APOSTAS
    ac = 0
    for i in range(n):
        for j in range(5):
            if v[i] == s[j]:
                ac += 1

# EXIBINDO OS RESULTADOS
    if par == 0:
        print('Apostador',k + 1,' número de acertos:',ac)
    else:
        print('Apostador',k+1,par)
