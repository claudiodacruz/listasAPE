'''
5 - Escreva uma função chamada primo para determinar se um número é primo ou não.
A função deve receber um número inteiro, retornar True se o número for primo,
ou False caso contrário. Escreva também um programa que, usando a função criada,
exiba os números primos entre 1 e 100.
'''

def primo(num):
    a = 0
    for i in range(num):
        div = num % (i + 1)
        if div == 0:
            a += 1
    if a <= 2:
        return True
    else:
        return False

n = 100
for i in range(100):
    if primo(i + 1):
        print (i+1, ' ',end='')

