'''
10. Escreva um programa que leia o arquivo gerado na questão 8 e copie os nomes
distribuindo para dois novos arquivos: machos.txt e femeas.txt (sendo um nome
por linha).
'''
arq = open('cadastro.txt','r')
mac = open('machos.txt','w')
fem = open('femeas.txt','w')
for linha in arq:
    dados = linha.split(',')
    nome = dados[0]
    sexo = dados[1]
    if sexo.upper() == 'M':
        mac.write(nome+'\n')
    else:
        fem.write(nome+'\n')
arq.close()
mac.close()
fem.close()
print('Arquivos gerados com sucesso')
 
