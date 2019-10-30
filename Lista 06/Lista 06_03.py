'''
3. Escreva um programa que leia do teclado o nome de um arquivo texto
e uma string, abra o arquivo e inclua no final dele a string lida.
'''

nomearq = input('Informe o nome do arquivo: ')
string = input('Digite um grupo de caracteres: ')
arq = open(nomearq+'.txt','a')
arq.write('\n'+string)
arq.close()
print('Inclusão realizada com sucesso!')
