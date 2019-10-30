'''
1. Dado o vetor A = { 6,3,8,7,2,5 } , escreva um programa que informe a soma
dos elementos do vetor A. Crie uma função soma que receba um vetor e retorne
a soma dos seus elementos.
'''

def soma(v):
    s = 0
    for n in v:
        s += n
    return s
vetor = [6,3,8,7,2,5]
print('Soma = ',soma(vetor))
print('Soma = ', sum(vetor))

      
 
