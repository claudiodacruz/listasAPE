'''
9. Escreva um programa que leia o arquivo gerado na questão 8 e calcule a média
de idade dos homens e a média de idade das mulheres.
'''

arq = open('cadastro.txt','r')
mac = open('machos.txt','w')
fem = open('femeas.txt','w')
m = 0
f = 0
somam = 0
somaf = 0
for linha in arq:
    dados = linha.split(',')
    nome = dados[0]
    sexo = dados[1]
    idade = int(dados[2])
    if sexo.upper() == 'M':
        m += 1
        somam += idade
        
    else:
        f += 1
        somaf += idade
        
arq.close()
mac.close()
fem.close()
print('Arquivos gerados com sucesso')
 

 
