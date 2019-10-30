'''
4. Escreva um programa que leia N números inteiros (máximo 20) e armazene em um
vetor X. Calcule a média dos elementos do vetor e informe quantos elementos
estão abaixo da média do conjunto. Crie uma função que faça a leitura dos
elementos de um vetor; uma função que retorne a média dos elementos de um vetor;
e, finalmente, outra função que receba um vetor e um número (float), e retorne
quantos elementos do vetor estão abaixo desse número.
'''

def ler_vetor(n):
    v = []
    for i in range(n):
        v.append(int(input()))
    return(v)

def media(v):
    return sum(v)/len(v)

def abaixo(v,x):
    cont = 0
    for e in v:
        if e < x:
            cont += 1
    return cont

quant = int(input('Quantidade de elementos (max.20): '))
vetor = ler_vetor(quant)
med = media(vetor)
nam = abaixo(vetor,med)
print('Vetor: ',vetor)
print('Média: ', med)
print('Quantidade de números abaixo da média: ',nam)
