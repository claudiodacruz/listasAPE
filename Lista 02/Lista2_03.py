'''
Escreva um programa que leia 3 números inteiros,
determine e mostre o maior deles.
'''
print('Digite 3 números inteiros diferentes')
num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
num3 = int(input('Digite o terceiro número:' ))
if (num1 > num2) and (num1 > num3):
    maior = num1
elif (num2 > num3):
    maior = num2
else:
    maior = num3
print('O maior número é {}.'.format(maior))

    
    
           
