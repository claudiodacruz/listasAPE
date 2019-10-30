'''
Escreva um programa que leia vários números, determine e mostre o maior
e o menor deles. A leitura do número zero encerra o programa.
'''

n =int(input('Digite um número: '))
maior = 0
menor = n
while n !=0:
    if n > maior:
        maior = n
    if n < menor:
        menor = n
    n =int(input('Digite um número: '))
print('O maior número informado foi {} e o menor {}.'.format(maior,menor))
