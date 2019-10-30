'''
1. Escreva um programa para ler e armazenar 10 números. Exiba: 
▪ Números que estão nos índices “par”;
▪ Números que estão nos índices “ímpar”.
'''

vi = []
vp = []
for i in range(10):
    num = int(input('Informe um número: '))
    if i % 2 ==0:
        vp.append(num)
    else:
        vi.append(num)
    vp.sort()
    vi.sort()
print(vp)
print(vi)

    
    
