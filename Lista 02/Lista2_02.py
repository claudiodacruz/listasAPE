'''
Escreva um programa que leia um número inteiro
e determine se ele é par ou ímpar.
'''
num1 = int(input('Digite um número inteiro: '))
par = num1 % 2
if (par == 0):
    print('O número {} é par.'.format(num1))
else:
    print('O número {} é ímpar.'.format(num1))

