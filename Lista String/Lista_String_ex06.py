'''
6. Faça um programa que leia uma frase e a exiba invertida.
'''

frase = input('Digite uma frase qualquer: ')
vetor = frase.split()
tam = len(vetor) - 1

for i in range(tam + 1):
    prmt = tam - i
    print(vetor[prmt], end =" ")

    
