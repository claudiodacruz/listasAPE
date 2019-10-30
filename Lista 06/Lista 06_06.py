'''
6. Escreva um programa que crie um arquivo texto
resultante da concatenação de dois outros arquivos.
'''

novo_arq1 = input('Informe o nome do primeiro arquivo: ')
novo_arq2 = input('Informe o nome do segundo arquivo: ')

arq1 = open(novo_arq1+'.txt','r')
arq2 = open(novo_arq2+'.txt','r')
novo = open('novo.txt','w')

novo1 = arq1.read()
novo2 = arq2.read()

novo.write(novo1)
novo.write(novo2)

arq1.close()
arq2.close()
novo.close()
print('Arquivo gerado com sucesso.')
