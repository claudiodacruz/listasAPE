'''
Escreva um programa que calcule e mostre o fatorial de um número N,
fornecido pelo usuário.
'''
print('Este programa calcula o fatorial de um número qualquer.')
n = int(input('Informe o número: '))
if n == 0 or n == 1:
    print('O fatorial de {} é = 1.'.format(n))
else:
    fat = 1    
    for i in range (n):
        fat = fat * (i+1)
    print('O fatorial de {} é = {}.'.format(n,fat))
