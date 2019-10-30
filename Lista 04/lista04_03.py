'''3 - Faça um programa que receba um vetor V de N números inteiros (N <= 100),
determine e exiba o maior e o menor elemento deste vetor e seus respectivos
índices.  OBS.: suponha a inexistência de valores repetidos.'''

n = int(input("Informe a quantidade de números: "))
v = []

#INCIANDO OS PARÂMETROS
num = int(input("Digite o número: "))
v.append(num)
maior = v[0]
menor = v[0]
indmax = 0
indmin = 0

#DEFINIDO O MAIOR E O MENOR
for i in range(1,n):
    num = int(input("Digite o número: "))
    v.append(num)
    if v[i] > maior:
        maior = v[i]
        indmax = i
    elif v[i] < menor:
        menor = v[i]
        indmin = i

#IMPRIMINDO OS RESULTADOS
print("Vetor: ", v)
print("O maior número é ", maior, "e o seu índice é ", indmax)
print("O menor número é ", menor, "e o seu índice é ", indmin)


