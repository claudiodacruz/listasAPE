'''
Escreva um programa que leia um número N, inteiro, e some todos os números
de 1 até N, mostrando o resultado.
'''
n = int(input('Informe um número inteiro: '))
soma = 0
for i in range(n):
    soma = soma + (i+1)
print('A soma de todos os números de 1 até {} é {}'.format(n,soma))
