'''
4. Escreva uma função chamada par que receba um número inteiro e retorne True
se o número for par ouFalse se for ímpar.Escreva também um programa que leia
vários números inteiros (encerrado com a leitura do valor 0)e, usando a função
criada, informe quantos números pares e quantos números ímpares foram lidos.
'''

#DEFINIÇÃO DA FUNÇÃO
def par(n):
    return n%2 == 0
'''
    if n%2 ==0:
        return True
    return False
'''

#Programa principal
num = 1
contpar=0
contimpar=0
print('Digite vários números inteiros (para encerrar digite "0")')
while num != 0:
    num = int(input('Digite um número: '))
    if par(num):
        contpar+=1
    else:
        contimpar+=1
print('Números pares: ',contpar)
print('Números impares: ',contimpar)
            

    
