''''1. Faça um programa que leia um vetor A de N números inteiros (N <= 100), e um outro inteiro
exiba um outro vetor B cujos elementos são os respectivos elementos de a multiplicados por K.
Ex: A = [1,2,3], K = 5, B = [5,10,15].'''

N = int(input('Inmforme o número de elementos do vetor.'))
K = int(input('Informe o multiplicador.'))

B = []
for i in range (N):
    num = int(input('Informe um número menor que 100.'))
    elem = K * num
    B.append(elem)
print(B)
