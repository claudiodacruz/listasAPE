'''
2. Escreva um programa que leia um vetor A com 10 números inteiros e informe o
maior elemento. Crie uma função maior que receba um vetor de inteiros e retorne
seu maior elemento.
'''

def maior(v):
    m = v[0]
    n = len(v)
    for i in range(1,n):
        if v[i] > m:
            m = v[i]
    return m

quant = 3
vetor = []
print('Digite ',quant,'números inteiros: ')
v = []
for i in range(quant):
    num = int(input('Informe o '+str(i+1)+'º número: '))
    v.append(num)
print('O maior número é: ',maior(v))
              
    

