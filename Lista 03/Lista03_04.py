'''
Considere H o somatório de 1/n com n variando de 1 a N. Escreva um programa que
calcule e mostre o valor de H, sabendo que o valor de N é inteiro e deverá ser
fornecido pelo usuário.
'''
n = int(input('Informe n: '))
soma = 0
for i in range(n):
    soma = soma + (1 / (i + 1))
print('O valor de H é: {:.4f}'.format(soma))
    
